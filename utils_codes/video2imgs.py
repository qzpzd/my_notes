# -*- coding: utf-8 -*-   
import os 
import cv2
import csv
import numpy as np
import concurrent.futures
 
def GetImgNameByEveryDir(file_dir,videoProperty):  
    FileNameWithPath = [] 
    FileName         = []
    FileDir          = []
    # videoProperty=['.png','jpg','bmp']
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] in videoProperty:  
                FileNameWithPath.append(os.path.join(root, file))  # 保存图片路径
                FileName.append(file)                              # 保存图片名称
                FileDir.append(root[len(file_dir):])               # 保存图片所在文件夹
    return FileName,FileNameWithPath,FileDir
 
# 以视频文件名创建文件夹，然后保存图像到对应文件夹
def AVI_To_Img_And_save(video_file):
	video_name = video_file.split('/')[-1].split('.')[0]
	print('当前处理的视频为：',video_file)
	cap = cv2.VideoCapture(video_file)
	rval = cap.isOpened()
	framenum=0
	while rval:
		rval, frame  = cap.read()
		if framenum%20!=0:
			framenum+=1
			continue
		save_dir     = 'E:/video16/'
		if not 	os.path.exists(save_dir):
			os.mkdir(save_dir)
		Img_savename = save_dir + '/' + 'hand_data_' + video_name + '_' + '%08d'%framenum +'.jpg'
		if rval:
			if os.path.exists(Img_savename)==False:
				cv2.imwrite(Img_savename, frame,[int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
		else:
			break
		framenum+=1
		print('正在处理视频{}的第{}帧,rval = {}...'.format(video_name,framenum,rval))
	cap.release()
	return ''
	
video_path = "E:/test/" 
FileName,FileNameWithPath,FileDir = GetImgNameByEveryDir(video_path,['.wmv','.mkv','.mp4'])
print('FileName = ',FileName)
# raise
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as process:
# with concurrent.futures.ProcessPoolExecutor(max_workers=batch_size) as process:
	process.map(AVI_To_Img_And_save,FileNameWithPath)
