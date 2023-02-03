import cv2
import numpy as np

videoLeft = cv2.VideoCapture("../mmpose/demo/resources/pose.processed.mov")
videoRight = cv2.VideoCapture("../pytorch-openpose/videos/pose.processed.mov")
videoLeft_ = cv2.VideoCapture("../lightweight-human-pose-estimation.pytorch/videos/pose.processed.mov")
videoRight_ = cv2.VideoCapture("../mediapipe/videos/pose.processed.mov")

width = (int(videoLeft.get(cv2.CAP_PROP_FRAME_WIDTH)))
height = (int(videoLeft.get(cv2.CAP_PROP_FRAME_HEIGHT)))



fps = int(videoLeft.get(5))
print(fps)
size = (int(width), int(height))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
videoWriter = cv2.VideoWriter("./result1.mp4", fourcc, fps, size)

def draw_text_line(img,text):
    y0,dy = 30,35
    for i, txt in enumerate(text.split('\n')):
        y = y0+i*dy
        cv2.putText(img, txt, (30, y), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0), 3)

while (videoLeft.isOpened() and videoRight.isOpened()):
    retLeft, frameLeft = videoLeft.read()
    retRight, frameRight = videoRight.read()
    retLeft_, frameLeft_ = videoLeft_.read()
    retRight_, frameRight_ = videoRight_.read()
    if(retLeft and retRight and retLeft_  and retRight_):

        frameLeft = cv2.resize(frameLeft, (int(width/2), int(height/2)), interpolation=cv2.INTER_CUBIC)
        draw_text_line(frameLeft,"mmpose \nfps=4.8")
        #cv2.putText(frameLeft,"fps=0.8",(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0), 3)
        frameRight = cv2.resize(frameRight, (int(width/2), int(height/2)), interpolation=cv2.INTER_CUBIC)
        draw_text_line(frameRight,"openpose \nfps=0.4")
        #cv2.putText(frameRight,"fps=0.4",(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0), 3)
        frameUp = np.hstack((frameLeft, frameRight))


        #再创建2个窗口，组成4个窗口
        frameLeft_ = cv2.resize(frameLeft_, (int(width/2), int(height/2)), interpolation=cv2.INTER_CUBIC)
        draw_text_line(frameLeft_,"lightpose \nfps=12")
        #cv2.putText(frameLeft_,"fps=12",(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0), 3)
        frameRight_ = cv2.resize(frameRight_, (int(width/2), int(height/2)), interpolation=cv2.INTER_CUBIC)
        draw_text_line(frameRight_,"mediapipe \nfps=13")
        #cv2.putText(frameRight_,"fps=13",(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0), 3)
        frameUp_ = np.hstack((frameLeft_, frameRight_))

        frame = np.vstack((frameUp, frameUp_))
        #print(frame.shape)

        cv2.imshow('frame', frame)
        videoWriter.write(frame)
    
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
videoWriter.release()
videoLeft.release()
videoRight.release()
videoLeft_.release()
videoRight_.release()
