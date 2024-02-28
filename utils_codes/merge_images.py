import os
import random
import cv2

# 设置文件夹路径
source_folder = 'C:/Users\suso\Desktop/baidu/yellow_orange'  # 存放要随机选取的图片的文件夹
target_images = 'C:/Users\suso\Desktop/baidu/frame_image'  # 存放目标图片的文件夹
new_labels = 'C:/Users\suso\Desktop/baidu/merege_yellow_orange_labels'  # 存放位置信息的文件夹
new_images = 'C:/Users\suso\Desktop/baidu/merege_yellow_orange_images'  # 存放目标图片的文件夹
os.makedirs(new_images, exist_ok=True)
os.makedirs(new_labels, exist_ok=True)

# 获取源文件夹中的所有图片文件
image_files = [f for f in os.listdir(source_folder) if f.endswith('.jpg')]

# 打开目标图片目录，遍历其中的每一张图片
for target_image_name in os.listdir(target_images):
    if target_image_name.endswith('.jpg'):
        # 随机选择几张图片
        num_images_to_select = random.randint(1, 3)  # 选择1-3张图片（可以根据需要更改）
        selected_images = random.sample(image_files, num_images_to_select)

        # 打开目标图片
        target_image_path = os.path.join(target_images, target_image_name)
        target_image = cv2.imread(target_image_path)
        height, width, _ = target_image.shape

        # 创建一个txt文件来存储YOLO格式的位置信息，与图像文件名一致
        txt_file_name = os.path.splitext(target_image_name)[0] + '.txt'
        txt_file_path = os.path.join(new_labels, txt_file_name)

        # 打开txt文件以写入位置信息
        with open(txt_file_path, 'w') as txt_file:
            for image_name in selected_images:
                # 随机缩放图片大小
                scale_factor1 = random.uniform(0.5, 1)
                scale_factor2 = random.uniform(0.5, 1)
                image = cv2.imread(os.path.join(source_folder, image_name))
                new_width = int(image.shape[1] * scale_factor1)
                new_height = int(image.shape[0] * scale_factor2)

                # 随机确定左上角坐标
                x_position = random.randint(0, width - new_width)  # 考虑边界
                y_position = random.randint(0, height - new_height)  # 考虑边界

                resized_image = cv2.resize(image, (new_width, new_height))

                # 将图片粘贴到目标图片上
                target_image[y_position:y_position + new_height, x_position:x_position + new_width] = resized_image

                # 记录位置信息到txt文件（使用YOLO格式）
                # class_id = 0  # 假设只有一个类别
                # x_center_rel = (x_position + new_width / 2) / width
                # y_center_rel = (y_position + new_height / 2) / height
                # width_rel = new_width / width
                # height_rel = new_height / height
                # txt_file.write(f"{class_id} {x_center_rel:.6f} {y_center_rel:.6f} {width_rel:.6f} {height_rel:.6f}\n")
                txt_file.write("")#空文件

        # 保存目标图片
        cv2.imwrite(os.path.join(new_images, target_image_name), target_image)
