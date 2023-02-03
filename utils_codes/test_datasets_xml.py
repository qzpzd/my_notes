import os,shutil
from tqdm import tqdm
import xml.dom.minidom
import cv2,glob

train_img_path = './dataset/20220324/trainval/'
test_img_path = './dataset/20220324/'

annotation_path = './dataset/20220324/Annotations/'

def label2Yolo_formate(xmin,ymin,xmax,ymax,img_w,img_h):
    x = 0.5*(xmax+xmin)/img_w
    y = 0.5*(ymax+ymin)/img_h
    w = (xmax-xmin)/img_w
    h = (ymax-ymin)/img_h
    return str(x),str(y),str(w),str(h)

def xml2YOLO_txt(img_path):
    for each_path in tqdm(list(filter(lambda x:'.jpg' in x ,os.listdir(img_path)))):
        
        img =cv2.imread(img_path+each_path)
        img_h,img_w,_ = img.shape
        xml_path = annotation_path+each_path.replace('.jpg','.xml')
        try:
            dom = xml.dom.minidom.parse(xml_path)
            root = dom.documentElement
            for i in range(len(dom.getElementsByTagName('object'))):
                xmin = int(dom.getElementsByTagName('xmin')[i].firstChild.data)
                ymin = int(dom.getElementsByTagName('ymin')[i].firstChild.data)
                xmax = int(dom.getElementsByTagName('xmax')[i].firstChild.data)
                ymax = int(dom.getElementsByTagName('ymax')[i].firstChild.data)
                # xmin = int(dom.getElementsByTagName('xmin')[0].firstChild.data)
                # ymin = int(dom.getElementsByTagName('ymin')[0].firstChild.data)
                # xmax = int(dom.getElementsByTagName('xmax')[0].firstChild.data)
                # ymax = int(dom.getElementsByTagName('ymax')[0].firstChild.data)
                x,y,w,h = label2Yolo_formate(xmin,ymin,xmax,ymax,img_w,img_h)

                with open('./dataset/20220324_yolo_format/train/labels/'+each_path.replace('.jpg','.txt'),'a') as f:
                    if i!=len(dom.getElementsByTagName('object'))-1:
                        f.write("0 {} {} {} {}\n".format(x,y,w,h))
                    else:
                        f.write("0 {} {} {} {}".format(x,y,w,h))

            shutil.copy(img_path+each_path,'./dataset/20220324_yolo_format/train/images/'+each_path)
        except Exception as e:
            print(e)
            if e.__class__.__name__=='FileNotFoundError':
                shutil.copy(img_path+each_path,'./dataset/20220324_yolo_format/no_label_imgs/'+each_path)

            elif e.__class__.__name__ =='IndexError':
                shutil.copy(img_path+each_path,'./dataset/20220324_yolo_format/no_head_imgs/'+each_path)

def show():
    image_dir = './dataset/20220324_yolo_format/train/images'
    label_dir = './dataset/20220324_yolo_format/train/labels'

    classes = ['head', 'baby', 'bag', 'hat', 'wallet', 'cellphone', 'glove',  'book',  'scarf', 'clothes', 'umbrella', 'dog', 'cat', 'belt']
    # cv2.namedWindow('test', cv2.WINDOW_NORMAL)
    class_to_name = {}
    dic = {}
    for img_path in glob.glob(image_dir + '/*.jpg'):
        _, jpg_name = os.path.split(img_path)
        label_path = os.path.join(label_dir, jpg_name.replace('jpg', 'txt'))
        im = cv2.imread(img_path)
        h, w, _ = im.shape
        class_loc = [list(map(float, each.strip().split())) for each in open(label_path, 'r').readlines()]
        for loc in class_loc:
            cls = classes[int(loc[0])]
            if cls not in dic:
                dic[cls] = 1
            else:
                dic[cls] += 1

            if cls not in class_to_name:
                class_to_name[cls] = [jpg_name]
            else:
                class_to_name[cls].append(jpg_name)

            x, y, w1, h1 = tuple(loc[1:])
            w2, h2 = int(w * w1) , int(h * h1)
            x1 = int(x * w) - int(w2 / 2)
            y1 = int(y * h) - int(h2 / 2)
            x2 = int(x * w) + int(w2 / 2)
            y2 = int(y * h) + int(h2 / 2)

            # cv2.putText(im, cls, (x1, y1), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 3)
            cv2.rectangle(im, (x1, y1), (x2, y2), (255, 0, 0), thickness=5)
        cv2.namedWindow('test',cv2.WINDOW_NORMAL)
        cv2.imshow('test', im)
        if cv2.waitKey(0) == ord('q'):  # q to quit
            raise StopIteration

# xml2YOLO_txt(test_img_path)
show()