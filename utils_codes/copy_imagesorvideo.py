from hashlib import new
import os
import shutil
import glob
import cv2

#-------------cope_image---------------------------------------
def cope_image():
    path = '/home/disk/qizhongpei/ssd_pytorch/接打电话告警/2022-07-22'# jpg/txt文件所在的当前文件夹
    new_path = '/home/disk/qizhongpei/ssd_pytorch/接打电话告警_copy/2022-07-22'# jpg/txt文件单独保存的文件夹

    if not os.path.exists(new_path):
        os.makedirs(new_path)
    for root, dirs, files in os.walk(path): # 提取文件夹下所有jpg文件复制转移到新的文件夹
        for i in range(len(files)):
            if files[i][-3:] == 'jpg' or files[i][-3:] == 'JPG': # 寻找当前文件下所有的jpg文件
            #if files[i][-3:] == ‘txt’ or files[i][-3:] == ‘TXT’:　# 寻找当前文件下所有的txt文件
                file_path = root + '/' + files[i]
                new_file_path = new_path + '/' + files[i]
                shutil.copy(file_path, new_file_path)

#-------------cope_video---------------------------------------
def cope_video():
    paths = '/home/disk/qizhongpei/ssd_pytorch/OMS_phone/误报/927_1026'# video文件所在的当前文件夹
    new_path = '/home/disk/qizhongpei/ssd_pytorch/OMS_phone/误报/927_1026/video'# jpg/txt文件单独保存的文件夹

    paths_ = os.listdir(paths)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    print(paths_)
    for path in paths_:
        for root, dirs, files in os.walk(os.path.join(paths+"/",path)): # 提取文件夹下所有video文件复制转移到新的文件夹
            for i in range(len(files)):
                if files[i][-3:] == 'mp4' or files[i][-3:] == 'MP4': # 寻找当前文件下所有的video文件
                #if files[i][-3:] == ‘txt’ or files[i][-3:] == ‘TXT’:　# 寻找当前文件下所有的txt文件
                    file_path = root + '/' + files[i]
                    new_file_path = new_path + '/' + files[i]
                    shutil.copy(file_path, new_file_path)
if __name__ =="__main__":
    cope_image()
    cope_video()