import os
import shutil 
import cv2

import numpy as np

path = "/home/disk/qizhongpei/projects/datasets/phone128/hand_others"
for image in os.listdir(path):
    imgpath = os.path.join(path, image)
    #print(imgpath)
    img = cv2.imread(imgpath)
    if img is None:
        print(imgpath)
        shutil.move(imgpath, f"/home/disk/qizhongpei/projects/datasets/phone128/none_img/{image}")
    # else:
    #     print("no none image")
    # cv2.imshow("im", imgpath)
print("测试完成")