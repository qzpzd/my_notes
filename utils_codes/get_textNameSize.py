import os, sys
import glob
from PIL import Image


img_dir = "/home/disk/yenanfei/phoneData_padding/JPEGImages/trainval"

img_lists = glob.glob(img_dir + '/*.jpg')


test_name_size = open('/home/disk/yenanfei/phoneData_padding/ImageSets/trainval_name_size_phone.txt', 'w')
i=0
for item in img_lists:
    try:
        img = Image.open(item)
        width, height = img.size
        temp1, temp2 = os.path.splitext(os.path.basename(item))
        test_name_size.write(temp1 + ' ' + str(height) + ' ' + str(width) + '\n')
    except Exception as e:
        line = item.split('/')[-1]
        with open ('train.txt','a') as f:
            f.write(line+'\n')

