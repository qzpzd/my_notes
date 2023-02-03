from tqdm import tqdm
import cv2
import glob
import numpy as np
video_paths = list(glob.iglob('/home/disk/qizhongpei/ssd_pytorch/linshi_img/*', recursive=True))

#save_video
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#fps = cap.get(cv2.CAP_PROP_FPS)
fps = 1
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
writer = cv2.VideoWriter("result.avi", fourcc, fps, (480, 480))
imgsz = 480

for i,video_path in enumerate(tqdm(video_paths)):
    cap = cv2.VideoCapture(video_path)
    
    while(True):
        ret, frame = cap.read()
        if (not ret):
            break
        img = cv2.resize(frame,(imgsz,imgsz))
        writer.write(img) 
writer.release()
cap.release()

import os

import cv2


def makeVideo(filelist, size):
    # filelist = os.listdir(path)
    # filelist2 = [os.path.join(path, i) for i in filelist]
    # print(filelist2)
    fps = 1  # 我设定位视频每秒1帧，可以自行修改
    # size = (1920, 1080)  # 需要转为视频的图片的尺寸，这里必须和图片尺寸一致
    video = cv2.VideoWriter("Video.avi", cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps,
                            size) 

    for item in filelist:
        print(item)
        if item.endswith('.jpg'):
            print(item)
            img = cv2.imread(item)
            img = cv2.resize(img,(480,480))
            video.write(img)

    video.release()
    cv2.destroyAllWindows()
    print('视频合成生成完成啦')


if __name__ == '__main__':
    path = list(glob.iglob('/home/disk/qizhongpei/ssd_pytorch/linshi_img/*', recursive=True))
    # 需要转为视频的图片的尺寸,必须所有图片大小一样，不然无法合并成功
    size = (480, 480)
    makeVideo(path, size)
