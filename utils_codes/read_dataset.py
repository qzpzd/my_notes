



from datasets.voc_data import VOCFormatDetectionDataset
import copy
import cv2

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
MEANS = (128, 128, 128)
SIZE = 128
labelmap=["phone","cell phone"]
# with open('data/hyp.scratch.yaml') as f:
#     hyp = yaml.load(f, Loader=yaml.FullLoader)  # load hyps

dataset=VOCFormatDetectionDataset(
            root='/home/disk/qizhongpei/DMS_phone/PhoneDataset_recut',
            #file_list='/home/disk/yenanfei/DMS_phone/PhoneDataset_recut/ImageSets/test_modified.txt',
            file_list='/home/disk/qizhongpei/DMS_phone/PhoneDataset_recut/ImageSets/test_modified.txt',
            img_size=128,
            batch_size=16,
            augment=True,
            hyp=None,
            rect=False,
            image_weights=False,
            cache_images=False,
            single_cls=False,
            stride=32,
            pad=0,
            rank=-1
            )
index=0
cv2.namedWindow('frame',0)
for data,objects,img_path,info in dataset:
    # bboxes=copy.copy(label[:,2:].float())
    # labels=copy.copy(label[:,1].float())
    print(img_path)
    #print(info)
    data=copy.copy(data)
    # objects=torch.cat([bboxes,labels.unsqueeze(1)],dim=1)
    # print(index)
    img = (data.permute(1, 2, 0).numpy()+128).astype('uint8').copy()
    #print(img.shape)
    # if label is None:
    #     continue
    # print(objects)
    if objects is not None:
        for i,obj in enumerate(objects):
            if obj is None:
                continue

            x1,y1,x2,y2,cls = obj
            cls=int(cls)
            # print(x1,x2,y1,y2)
            if (x1.item() - x2.item()!=0):
                cv2.rectangle(img,(int(x1*img.shape[1]), int(y1*img.shape[0])),(int(x2*img.shape[1]), int(y2*img.shape[0])), COLORS[cls % 9], 1)
                cv2.putText(img, labelmap[cls], (int(x1*img.shape[1]), int(y1*img.shape[0])),cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[cls % 9], 1, cv2.LINE_AA)
    cv2.imshow('frame',img)
    if cv2.waitKey(0)&0xFF==ord('q'):
        break

    index=index+1
