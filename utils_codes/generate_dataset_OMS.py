import argparse
import imp

from numpy.core.arrayprint import printoptions
import onnxruntime
import cv2
import numpy as np
import os,sys
import glob
import torch
import time
import torchvision
import glog,copy
from tqdm import tqdm
CAFFE_ROOT = '/home/disk/tanjing/ambacaffe'
if os.path.join(CAFFE_ROOT, 'python') not in sys.path:
    sys.path.insert(0, os.path.join(CAFFE_ROOT, 'python'))
import caffe

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


#-----------------landmarks_detect-------------------------------------------
model_def = "prnet128_256_focus_defocus_4d_stream.prototxt"
model_weights = "prnet128_exp154.caffemodel"
boxnet = caffe.Net(model_def,model_weights,caffe.TEST)

def detect_lmk(bbox,img):
    face_crop = img[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
    point3d = get_point3d(boxnet,face_crop)
    point3d = point3d + np.array([int(bbox[0]),int(bbox[1]),0]).reshape(-1,3)
    for i,point2d in enumerate(point3d[:,0:2]):
        point2d = point2d.astype(int)
        cv2.circle(img,(point2d[0],point2d[1]),2,(0,255,0))

def get_lmk(bbox,img):
    points = []
    face_crop = img[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
    point3d = get_point3d(boxnet,face_crop)
    point3d = point3d + np.array([int(bbox[0]),int(bbox[1]),0]).reshape(-1,3)
    for i,point2d in enumerate(point3d[:,0:2]):
        point2d = point2d.astype(int)
        points.append([point2d[0],point2d[1]])
    points = np.array(points)
    return points

def get_point3d(net,image):
    height,width,channel = image.shape
    image = cv2.resize(image,(128,128))  
    if image.ndim == 3 and channel == 3:
        image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    if image.ndim==2:
        image=image[:,:,np.newaxis]
    net_input=(torch.from_numpy(np.transpose(image,(2,0,1))).unsqueeze(0).cuda()-128.0)/128.0   
    face_input_numpy = net_input.cpu().float().numpy().copy()
    net.blobs['data'].data[:] = face_input_numpy.copy()[:].astype('float64')
    net.forward()
    caffe_pred=net.blobs['interp10'].data.copy()[0]
    pos_map=np.transpose(caffe_pred,(1,2,0))

    uv_kpt_ind = np.fromfile('uv_kpt_ind_lm67.txt',sep=' ').reshape(2,-1).astype(int)
    lmk67_temp = pos_map[uv_kpt_ind[1,:], uv_kpt_ind[0,:], :]
    lmk67_3d=(lmk67_temp*np.array([width,height,1]).reshape(-1,3)).astype(int)

    return lmk67_3d


#---------------------NMS--------------------------------------------------------------------
def non_max_suppression(prediction, conf_thres=0.25, iou_thres=0.45, classes=None, agnostic=False, multi_label=False,
                        labels=()):

    nc = prediction[0].shape[1] - 5  # number of classes
    xc = prediction[..., 4] > conf_thres  # candidates

    # Settings
    min_wh, max_wh = 2, 4096  # (pixels) minimum and maximum box width and height
    max_det = 300  # maximum number of detections per image
    max_nms = 30000  # maximum number of boxes into torchvision.ops.nms()
    time_limit = 10.0  # seconds to quit after
    redundant = True  # require redundant detections
    multi_label &= nc > 1  # multiple labels per box (adds 0.5ms/img)
    merge = False  # use merge-NMS

    t = time.time()
    output = [torch.zeros((0, 6), device=prediction.device)] * prediction.shape[0]
    for xi, x in enumerate(prediction):  # image index, image inference
        # Apply constraints
        # x[((x[..., 2:4] < min_wh) | (x[..., 2:4] > max_wh)).any(1), 4] = 0  # width-height
        x = x[xc[xi]]  # confidence

        # Cat apriori labels if autolabelling
        if labels and len(labels[xi]):
            l = labels[xi]
            v = torch.zeros((len(l), nc + 5), device=x.device)
            v[:, :4] = l[:, 1:5]  # box
            v[:, 4] = 1.0  # conf
            v[range(len(l)), l[:, 0].long() + 5] = 1.0  # cls
            x = torch.cat((x, v), 0)

        # If none remain process next image
        if not x.shape[0]:
            continue

        # Compute conf
        x[:, 5:] *= x[:, 4:5]  # conf = obj_conf * cls_conf

        # Box (center x, center y, width, height) to (x1, y1, x2, y2)
        box = xywh2xyxy(x[:, :4])

        # Detections matrix nx6 (xyxy, conf, cls)
        if multi_label:
            i, j = (x[:, 5:] > conf_thres).nonzero(as_tuple=False).T
            x = torch.cat((box[i], x[i, j + 5, None], j[:, None].float()), 1)
        else:  # best class only
            conf, j = x[:, 5:].max(1, keepdim=True)
            x = torch.cat((box, conf, j.float()), 1)[conf.view(-1) > conf_thres]

        # Filter by class
        if classes is not None:
            x = x[(x[:, 5:6] == torch.tensor(classes, device=x.device)).any(1)]

        # Apply finite constraint
        # if not torch.isfinite(x).all():
        #     x = x[torch.isfinite(x).all(1)]

        # Check shape
        n = x.shape[0]  # number of boxes
        if not n:  # no boxes
            continue
        elif n > max_nms:  # excess boxes
            x = x[x[:, 4].argsort(descending=True)[:max_nms]]  # sort by confidence

        # Batched NMS
        c = x[:, 5:6] * (0 if agnostic else max_wh)  # classes
        boxes, scores = x[:, :4] + c, x[:, 4]  # boxes (offset by class), scores
        i = torchvision.ops.nms(boxes, scores, iou_thres)  # NMS
        if i.shape[0] > max_det:  # limit detections
            i = i[:max_det]
        if merge and (1 < n < 3E3):  # Merge NMS (boxes merged using weighted mean)
            # update boxes as boxes(i,4) = weights(i,n) * boxes(n,4)
            iou = box_iou(boxes[i], boxes) > iou_thres  # iou matrix
            weights = iou * scores[None]  # box weights
            x[i, :4] = torch.mm(weights, x[:, :4]).float() / weights.sum(1, keepdim=True)  # merged boxes
            if redundant:
                i = i[iou.sum(1) > 1]  # require redundancy

        output[xi] = x[i]
        if (time.time() - t) > time_limit:
            print(f'WARNING: NMS time limit {time_limit}s exceeded')
            break  # time limit exceeded

    return output

def xywh2xyxy(x):
    # Convert nx4 boxes from [x, y, w, h] to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
    y = torch.zeros_like(x) if isinstance(x, torch.Tensor) else np.zeros_like(x)
    y[:, 0] = x[:, 0] - x[:, 2] / 2  # top left x
    y[:, 1] = x[:, 1] - x[:, 3] / 2  # top left y
    y[:, 2] = x[:, 0] + x[:, 2] / 2  # bottom right x
    y[:, 3] = x[:, 1] + x[:, 3] / 2  # bottom right y
    return y

#---------------------img_preprocess-----------------------------------------------------------------
def img_preprocess(frame,imgsz):
    img = cv2.resize(frame,(imgsz,imgsz))
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_gray = img_gray[:,:,np.newaxis]
    img = np.concatenate((img_gray, img_gray, img_gray), axis=-1)
    img = img[:, :, ::-1].transpose(2, 0, 1).astype('float32')[np.newaxis, :, :, :]  
    img /= 255.0  
    return img

#---------------------face_detect----------------------------------------------------------------------------
def face_detect(img):
    pred = session.run(out_name,{in_name: img})
    
    grid = [torch.zeros(1)] * 3
    z = []
    shapelist = [60,30,15]
    for i in range(len(pred)):
        pred[i] = torch.from_numpy(pred[i]).to(device)
        pred[i] = torch.reshape(pred[i],(1,3,shapelist[i],shapelist[i],6))  
        bs, na, ny, nx, no = pred[i].size()
        if grid[i].shape[2:4] != pred[i].shape[2:4]:
            grid[i] = make_grid(nx, ny).to(device)

        y = pred[i].sigmoid()
        y[..., 0:2] = (y[..., 0:2] * 2. - 0.5 + grid[i].to(device)) * stride[i]  # xy
        y[..., 2:4] = (y[..., 2:4] * 2) ** 2 * anchor_grid[i]  # wh
        z.append(y.view(1, -1, no))
    pred = torch.cat(z, 1)
    pred = non_max_suppression(pred, conf_thres=0.5, iou_thres=0.45)[0]
    return pred

def make_grid(nx=20, ny=20):
    yv, xv = torch.meshgrid([torch.arange(ny), torch.arange(nx)])
    return torch.stack((xv, yv), 2).view((1, 1, ny, nx, 2)).float()

def scale_ratio(each,frame,imgsz):
    ratio = (frame.shape[0] /imgsz , frame.shape[1] / imgsz)
    each[[0, 2]] *= ratio[1]
    each[[1, 3]] *= ratio[0]
    return each
#--------------------bbox_enlarger-------------------------------------------------------------------    
def bbox_enlarger(im0,bbox,scale):
    w = bbox[2]-bbox[0]+1
    h = bbox[3]-bbox[1]+1

    bbox[0] = bbox[0]-h*scale[0]
    bbox[2] = bbox[2]+w*scale[0]
    bbox[3] = bbox[3]+h*scale[1]
    
    bbox[0].clamp_(0, im0.shape[1])
    bbox[1].clamp_(0, im0.shape[0])
    bbox[2].clamp_(0, im0.shape[1])
    bbox[3].clamp_(0, im0.shape[0])

    return bbox


#--------------------crop_calling_area-------------------------------------------------------------------
def bbox_from_points(points):#获取landmark外接矩形框
    max_=np.max(points,axis=0)
    min_=np.min(points,axis=0)
    return [min_[0],min_[1],max_[0],max_[1]]

def crop_calling_area(lmks,h,w):
    eye_index = [41,37,28,32]
    center = np.mean(lmks[eye_index,:],axis = 0) 
    face_bbox=bbox_from_points(lmks)
    bbox_w = face_bbox[2]-face_bbox[0]
    bbox_h = face_bbox[3]-face_bbox[1]
    x0 =  np.clip(face_bbox[0] -1*bbox_w,0,w)
    y0 =  np.clip(face_bbox[1] - 0.5*bbox_h,0,h)
    x1 =  np.clip(face_bbox[2] + 1*bbox_w,0,w)
    y1=  np.clip(face_bbox[3] + 0.5*bbox_h,0,h)
    return [x0,y0,x1,y1]
#-----------------------face_model--------------------------------------------------------------------------    
face_model = "exp8_best.onnx"
session = onnxruntime.InferenceSession(face_model)
in_name = [input.name for input in session.get_inputs()][0]
out_name = [output.name for output in session.get_outputs()]

imgsz = 480
stride = [8, 16, 32] 
anchor_grid = torch.tensor([[[[[[10., 13.]]], [[[16., 30.]]], [[[33., 23.]]]]],
                      [[[[[30., 61.]]], [[[62., 45.]]], [[[59., 119.]]]]],
                      [[[[[116., 90.]]], [[[156., 198.]]], [[[373., 326.]]]]]]).to(device)
#-------------------------------------------------------
from PIL import Image, ImageDraw, ImageFont
def drawBBox(frame,bbox,name):
  cv2.rectangle(frame,(int(bbox[0]),int(bbox[1])),(int(bbox[2]),int(bbox[3])),(0,255,255),2)
  cv2.putText(frame, name, (int(bbox[0]),int(bbox[1]-10)), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255),1)
  cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  pilimg = Image.fromarray(cv2img)
  draw = ImageDraw.Draw(pilimg)

  # for i in range(0,len(bbox)):
  font = ImageFont.truetype("calibrii_____.ttf", 50, encoding="utf-8")
  draw.text((int(bbox[0]),int(bbox[3]+20)), name, (0,0,255), font=font)
  
  frame = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
  return frame

#-----------------------IOU--------------------------------------------------------------------------    

def compute_iou(rec1, rec2):
    """
    computing IoU
    :param rec1: (x0, y0, x1, y1), which reflects
            (left,top, right, bottom)
    :param rec2: (x0, y0, x1, y1)
    :return: scala value of IoU
    """
    # computing area of each rectangles
    S_rec1 = (rec1[3] - rec1[1]) * (rec1[2] - rec1[0])
    S_rec2 = (rec2[3] - rec2[1]) * (rec2[2] - rec2[0])
 
    # computing the sum_area
    sum_area = S_rec1 + S_rec2
 
    # find the each edge of intersect rectangle
    left_line = max(rec1[0], rec2[0])
    right_line = min(rec1[2], rec2[2])
    top_line = max(rec1[1], rec2[1])
    bottom_line = min(rec1[3], rec2[3])
 
    # judge if there is an intersect
    if left_line >= right_line or top_line >= bottom_line:
        return 0
    else:
        intersect = (right_line - left_line) * (bottom_line - top_line)
        return (intersect / (sum_area - intersect))*1.0
#-----------------------Json information--------------------------------------------------------------------------    
import json
def json_info(frame,json_path):
    image = frame
    face_coord={}
    with open(str(json_path),'r') as f:
        json_data = json.load(f)
        flage = False
        for data in json_data['BlockDatas']:
            if "RectElementData" in data["__type"]:
                face_id = int(data["GroupID"])
                height = data["Rectangle"]["_height"]
                width = data["Rectangle"]["_width"]
                x1 = data["Rectangle"]["_x"]
                y1 = data["Rectangle"]["_y"]
                x2 = x1+width
                y2 = y1+height

                face_coord[face_id]=([int(x1), int(y1),int(x2), int(y2)])
                # COLORS = [(255, 255, 0), (0, 255, 0), (0, 0, 255)]
                # cv2.rectangle(image,(int(x1), int(y1)),(int(x2), int(y2)), COLORS[2], 3)
            if "PolygonElementData" in data["__type"]:
                groupid = int(data["GroupID"])
                vertexs = data["Vertexs"]
                flage = True
        if flage:
            return image,face_coord,groupid,vertexs
        return image,face_coord,None,None

#----------------------------------------------------------------------------------------------
def drawLM(frame,lm,color=(0,255,0)):
    r=4
    for i in lm:
        point=[i["X"],i["Y"]]
        print('point',point)
        cv2.circle(frame,(int(point[0]),int(point[1])),r,color,-1)
#----------------------------------------------------------------------------------------------
from xml.dom import minidom
import cv2
import os,shutil

def findrange(x,minx,maxx):
    a = x
    if x<minx:
        a = minx
    if x>maxx:
        a = maxx
    return a

def write_xml(phone_box,cult_fram,cult_fram_name,xml_savePath):
    try:

        img_name = cult_fram_name
        xml_name = img_name.replace('.jpg','.xml')
        floder = cult_fram_name

        w = cult_fram.shape[1]
        h = cult_fram.shape[0]
        d = cult_fram.shape[2]
        # print w,h,d
        #print('i=', i)
        doc = minidom.Document()  

        annotation = doc.createElement('annotation')  
        doc.appendChild(annotation)  

        folder = doc.createElement('folder')
        folder.appendChild(doc.createTextNode(floder))  
        annotation.appendChild(folder)  

        filename = doc.createElement('filename')
        filename.appendChild(doc.createTextNode(img_name))
        annotation.appendChild(filename)

        # filename = doc.createElement('path')
        # filename.appendChild(doc.createTextNode(jpg_dirtory))
        # annotation.appendChild(filename)

        source = doc.createElement('source')
        database = doc.createElement('database')
        database.appendChild(doc.createTextNode("Unknown"))
        source.appendChild(database)
        annotation.appendChild(source)


        size = doc.createElement('size')
        width = doc.createElement('width')
        width.appendChild(doc.createTextNode("%d" % w))
        size.appendChild(width)
        height = doc.createElement('height')
        height.appendChild(doc.createTextNode("%d" % h))
        size.appendChild(height)
        depth = doc.createElement('depth')
        depth.appendChild(doc.createTextNode("%d" % d))
        size.appendChild(depth)
        annotation.appendChild(size)

        segmented = doc.createElement('segmented')
        segmented.appendChild(doc.createTextNode("0"))
        annotation.appendChild(segmented)

        label = ['phone','background']
        mark = label[0]

        if phone_box!=[]:
            x0,y0,x1,y1 = phone_box
            x0 = findrange(x0,0,w)
            y0 = findrange(y0,0,h)
            x1 = findrange(x1,0,w)
            y1 = findrange(y1,0,h)   
            
            box = [int(x0),int(y0),int(x1),int(y1)]
            
            
            if box[2]-box[0]<=0 or box[3]-box[1]<=0:
                return
  
            object = doc.createElement('object')
            nm = doc.createElement('name')
            nm.appendChild(doc.createTextNode(mark))
            object.appendChild(nm)
            pose = doc.createElement('pose')
            pose.appendChild(doc.createTextNode("Unspecified"))
            object.appendChild(pose)
            truncated = doc.createElement('truncated')
            # truncated.appendChild(doc.createTextNode("1"))
            truncated.appendChild(doc.createTextNode(mark))
            object.appendChild(truncated)
            difficult = doc.createElement('difficult')
            difficult.appendChild(doc.createTextNode('0'))
            object.appendChild(difficult)

            #  simple

            bndbox = doc.createElement('bndbox')
            # xmin ymin
            xmin = doc.createElement('xmin')
            xmin.appendChild(doc.createTextNode("%d" % box[0]))
            bndbox.appendChild(xmin)

            ymin = doc.createElement('ymin')
            ymin.appendChild(doc.createTextNode("%d" % box[1]))
            bndbox.appendChild(ymin)

            # xmax ymin
            xmax = doc.createElement('xmax')
            xmax.appendChild(doc.createTextNode("%d" % box[2]))
            bndbox.appendChild(xmax)

            ymax = doc.createElement('ymax')
            ymax.appendChild(doc.createTextNode("%d" % box[3]))
            bndbox.appendChild(ymax)

            #+++++++++++++++++++++++++++++++++++++++++++++++++
            object.appendChild(bndbox)
            annotation.appendChild(object)

        savefile = open(xml_savePath+xml_name, 'w')
        savefile.write(doc.toprettyxml())
        savefile.close()

    except Exception as e:
        print(e)
        
#----------------------------------------------------------------------------------------------
def dict2json(file_name,the_dict):
    '''
    将字典文件写如到json文件中
    :param file_name: 要写入的json文件名(需要有.json后缀),str类型
    :param the_dict: 要写入的数据，dict类型
    :return: 1代表写入成功,0代表写入失败
    '''
    try:
        json_str = json.dumps(the_dict,indent=4,ensure_ascii=False)
        with open(file_name, 'w') as json_file:
            json_file.write(json_str)
        return 1
    except:
        return 0
#----------------------------------------------------------------------------------------------


video_paths = list(glob.iglob('/home/disk/yenanfei/OMS_phone/OMS_phone_data/oms打电话20211015/*.jpg', recursive=True))

for video_path in tqdm(video_paths):
    # video_path="/home/disk/yenanfei/OMS_phone/OMS_phone_data/oms打电话210923/2185_886_0526_3_765.jpg"
    print(video_path)
    image_name = os.path.basename(video_path)
    json_path = video_path.replace('.jpg','.json')
    lmks_path = video_path.replace('.jpg','_lmks.json')
    cap = cv2.VideoCapture(video_path)
    # save_video_path = video_path.replace('images','test')    
    # fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    # fps = cap.get(cv2.CAP_PROP_FPS)
    # size = (1920,1080)
    # out = cv2.VideoWriter(save_video_path,fourcc,int(fps),size)    
    # ret, frame = cap.read()
    # while(True):
    ret, frame = cap.read()
    if (not ret):
        break 
    
    frame,face_coord,groupid,vertexs = json_info(frame,json_path)
    # drawLM(frame,vertexs)
    # cv2.imshow('a',frame)
    # cv2.waitKey(0)
    
    height,width,ch=frame.shape
    img = img_preprocess(frame,imgsz)
    pred = face_detect(img)    

    lmk_dict={}
    for each in pred:
        each = scale_ratio(each,frame,imgsz)
        bbox = bbox_enlarger(frame,each,scale=[0.07,0.07])

        lmks = get_lmk(bbox,frame)
        lmks_box= bbox_from_points(lmks)
        # cv2.rectangle(frame, (int(lmks_box[0]), int(lmks_box[1])), (int(lmks_box[2]), int(lmks_box[3])), (0, 255, 0), 3)

        area = crop_calling_area(lmks,height,width)
        cult_fram = frame[int(area[1]):int(area[3]),int(area[0]):int(area[2])] 
        

        for key,value in face_coord.items():
            cult_fram_name = image_name.replace('.jpg','_'+str(key)+'.jpg')
            save_path='./OMS_phone_data/phone_20211015/no_phone/'
            phone_box=[]

            if compute_iou(value,lmks_box)>=0.4:
                lmk_dict[key] = lmks.tolist()
                if groupid == key:
                    X=[]
                    Y=[]
                    for points in vertexs:
                        points["X"] = np.clip(points["X"]-area[0],0,area[2]-area[0])
                        points["Y"] = np.clip(points["Y"]-area[1],0,area[3]-area[1])
                        X.append(points["X"])
                        Y.append(points["Y"])

                    phone_box=[min(X),min(Y),max(X),max(Y)]

                    save_path='./OMS_phone_data/phone_20211015/phone/'

                xml_savePath = save_path+'Annotations/'
                img_savePath = save_path+'JPEGImages/'

                if not os.path.isdir(xml_savePath):
                    os.mkdir(xml_savePath)

                if not os.path.isdir(img_savePath):
                    os.mkdir(img_savePath)

                write_xml(phone_box,cult_fram,cult_fram_name,xml_savePath)
                cv2.imwrite(img_savePath+cult_fram_name,cult_fram)

                del face_coord[key]
                # cv2.imshow('a',cult_fram)
                # cv2.waitKey(0)
                break
    
    dict2json(lmks_path,lmk_dict)
    cap.release()



