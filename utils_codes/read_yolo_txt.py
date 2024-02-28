import numpy as np
import cv2
import torch

source_directory_img_path= '/home/disk/qizhongpei/projects/yolov5/fire/data/images'
source_directory_label_path= '/home/disk/qizhongpei/projects/yolov5/fire/data/label_txt'
target_directory_path= '/home/disk/qizhongpei/projects/yolov5/fire/data/output'
dic={}

#坐标转换，原始存储的是YOLOv5格式
# Convert nx4 boxes from [x, y, w, h] normalized to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
def xywhn2xyxy(x, w=640, h=640, padw=0, padh=0):

    y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
    y[:, 0] = w * (x[:, 0] - x[:, 2] / 2) + padw  # top left x
    y[:, 1] = h * (x[:, 1] - x[:, 3] / 2) + padh  # top left y
    y[:, 2] = w * (x[:, 0] + x[:, 2] / 2) + padw  # bottom right x
    y[:, 3] = h * (x[:, 1] + x[:, 3] / 2) + padh  # bottom right y
    return y

import os
def draw_label(image_path,label_path):
    if os.path.getsize(label_path)>0:
        with open(label_path, 'r') as f:
            lb = np.array([x.split() for x in f.read().strip().splitlines()], dtype=np.float32)
        # 读取图像文件
        img = cv2.imread(str(image_path))
        h, w = img.shape[:2]
        lb[:, 1:] = xywhn2xyxy(lb[:, 1:], w, h, 0, 0)  # 反归一化
        #print(lb)


        for _, x in enumerate(lb):
            class_label = int(x[0])
            if class_label == 14 :
                print(label_path)
            if class_label in dic:
                dic[class_label]+=1
            else:
                dic[class_label]=1 #count the number of labels
                
        # 绘图
            cv2.rectangle(img, (int(x[1]), int(x[2])), (int(x[3]), int(x[4])), (0, 255, 0))
            cv2.putText(img, str(class_label), (int(x[1]), int(x[2] - 2)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=(0, 0, 255), thickness=2)
            cv2.imshow("image",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return     img




if __name__ == '__main__':
    for root, dirs, files in os.walk(source_directory_img_path):

            for f in files:
                
                file_name = f.split('.jpg')[0]+".txt"
                image_path = os.path.join(source_directory_img_path, f)
                print(image_path)
                label_path =os.path.join(source_directory_label_path, file_name)
                target =os.path.join(target_directory_path, f)
                img= draw_label(image_path, label_path)

                # cv2.imwrite(target, img)
    print(dic)


