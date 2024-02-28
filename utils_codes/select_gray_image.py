import cv2
import os
import shutil

# 定义原始文件夹和目标文件夹路径
source_folder = 'F:\Download\Fire_Detection.v2i.yolov5pytorch/valid/images'
label_folder = 'F:\Download\Fire_Detection.v2i.yolov5pytorch/valid/labels'
target_image_folder = 'F:\Download\Fire_Detection.v2i.yolov5pytorch/valid/gray_images'
target_txt_folder = 'F:\Download\Fire_Detection.v2i.yolov5pytorch/valid/gray_labels'

# 创建目标文件夹（如果不存在）
os.makedirs(target_image_folder, exist_ok=True)
os.makedirs(target_txt_folder, exist_ok=True)

# 遍历原始文件夹中的所有文件
for filename in os.listdir(source_folder):
    if filename.endswith('.jpg'):  # 仅处理jpg图像文件
        image_path = os.path.join(source_folder, filename)

        # 读取图像
        image = cv2.imread(image_path)

        # 检查图像是否是三通道
        if image.shape[2] == 3:
            # 计算第一个通道减去第二个通道的差值并求均值
            channel_diff = image[:, :, 0].astype(int) - image[:, :, 1].astype(int)
            mean_diff = channel_diff.mean()
            print(image[:, :, 0])
            print(image[:, :, 1])

            # 如果均值为0，则移动图像和对应的txt文件
            if mean_diff == 0:
                # 构建对应的txt文件路径
                txt_filename = os.path.splitext(filename)[0] + '.txt'
                txt_path = os.path.join(label_folder, txt_filename)

                # 移动图像和txt文件到目标文件夹
                shutil.move(image_path, os.path.join(target_image_folder, filename))
                shutil.move(txt_path, os.path.join(target_txt_folder, txt_filename))

# 完成后，目标文件夹中包含了满足条件的图像和对应的txt文件
