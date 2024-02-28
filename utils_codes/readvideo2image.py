import cv2
import os

# 打开视频文件
video_capture = cv2.VideoCapture('D:\Tencent\Documents\WXWork/1688856165390184\Cache\Video/2023-09/VID_20230904_141712.mp4')  # 将 'video.mp4' 替换为你的视频文件路径

# 检查视频文件是否成功打开
if not video_capture.isOpened():
    print("无法打开视频文件")
    exit()

# 循环读取视频帧
frame_count = 3070 # 用于计数帧数
while True:
    ret, frame = video_capture.read()  # 读取一帧

    if not ret:
        break  # 如果读取完所有帧，退出循环

    frame_count += 1

    # 在这里可以对帧进行处理，如果不需要处理，可以跳过这一部分

    # 保存单帧图片
    image_path = 'F:\Download\Fire_Source_Detection/train/frame_image_1'
    frame_filename = f"20230908_frame_{frame_count}.jpg"  # 图片文件名，可以根据需要自定义
    frame_filename = os.path.join(image_path,frame_filename)
    cv2.imwrite(frame_filename, frame)

    # 在窗口中显示当前帧（可选）
    cv2.imshow('Frame', frame)
    
    # 按'q'键退出显示窗口
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 释放视频捕获对象和销毁显示窗口（如果有的话）
video_capture.release()
cv2.destroyAllWindows()
