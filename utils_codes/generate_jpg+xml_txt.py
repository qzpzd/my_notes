# -*- coding:UTF-8 -*-  
import os,sys
import glob
from tqdm import tqdm
trainval_dir = "/home/disk/qizhongpei/ssd_pytorch/OMS_phone/接打电话告警_video/上海_0928/"
# test_dir = "/home/disk/yenanfei/OMS_phone/OMS_phone_data/phone_20211015/phone/test"

trainval_img_lists = glob.glob(trainval_dir + '/*.jpg')
trainval_img_names = []
for item in trainval_img_lists:
    temp1, temp2 = os.path.splitext(os.path.basename(item))
    trainval_img_names.append(temp1)

# test_img_lists = glob.glob(test_dir + '/*.jpg')
# test_img_names = []
# for item in test_img_lists:
#     temp1, temp2 = os.path.splitext(os.path.basename(item))
#     test_img_names.append(temp1)

dist_img_dir = "JPEGImages"
dist_anno_dir = "Annotations"

trainval_fd = open("/home/disk/qizhongpei/DMS_phone/PhoneDataset_recut_change/ImageSets/trainval_Negative_上海_0928.txt", 'w')
# test_fd = open("/home/disk/yenanfei/OMS_phone/OMS_phone_data/phone_20211015/phone/test.txt", 'w')

# f = open ('delete.txt')
# words=[]
# for line in f.readlines():
#     words.append(line.strip())

for item in tqdm(trainval_img_names):
#     if str(item) + '.jpg' in words:
#         continue
#     else:
    trainval_fd.write(dist_img_dir+'/'+str(item) + '.jpg '+dist_anno_dir+'/'+str(item) + '.xml\n')

# for item in tqdm(test_img_names):
#     test_fd.write(dist_img_dir+'/'+str(item) + '.jpg '+dist_anno_dir+'/'+str(item) + '.xml\n')
