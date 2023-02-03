import os
import cv2
def save_img():
    video_path = "/home/disk/qizhongpei/ssd_pytorch/OMS_phone/误报/11_14/video/"
    videos = os.listdir(video_path)
    # print(len(videos))
    # exit(0)
    for video_name in videos:
        
        file_name = video_name
        print(file_name)
        folder_name = video_path + file_name
        folder_name,_ = os.path.splitext(folder_name)
        os.makedirs(folder_name)
        print(video_path+'/'+video_name)
        vc = cv2.VideoCapture(video_path+'/'+video_name) 
        c=0
        rval=vc.isOpened()

        while rval:   
            c = c + 1
            rval, frame = vc.read()
            pic_path = folder_name+'/'
            if rval:
                cv2.imwrite(pic_path + video_name+'_'+ str(c) + '.jpg', frame)
                cv2.waitKey(1)
            else:
                break
        vc.release()
        print('save_success')
        print(folder_name)
save_img()