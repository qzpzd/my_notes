import os
import cv2
import imutils
import numpy as np
img_dir = 'H://frg'#拼接图像的文件夹路劲
names = os.listdir(img_dir)
images = []
for name in names:
    img_path = os.path.join(img_dir, name)
    image = cv2.imread(img_path)
    #image = cv2.resize(image,(1919,1078))
    images.append(image)
stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
status, stitched = stitcher.stitch(images)
print(status)
if status==0:
    print(1)
    cv2.imwrite('H:\stitch_2.jpg', stitched)#保存拼接图像
