import os
import random
import shutil

# 源文件夹，包含200张图片
source_folder = '/home/disk/qizhongpei/projects/yolov5/fire/data/20231109/pos_small/merege_small_images'

# 目标文件夹，包含标签文件，文件名与图片文件名对应
label_folder = '/home/disk/qizhongpei/projects/yolov5/fire/data/20231109/pos_small/merege_small_labels'

# 目标文件夹，用于存储随机选取的200张图片和对应的标签
destination_image_folder = '/home/disk/qizhongpei/projects/yolov5/fire/data/20231109/pos_small/200_red_images'
destination_label_folder = '/home/disk/qizhongpei/projects/yolov5/fire/data/20231109/pos_small/200_red_labels'

os.makedirs(destination_image_folder, exist_ok=True)
os.makedirs(destination_label_folder, exist_ok=True)

# 获取源文件夹中的所有图片文件
image_files = [f for f in os.listdir(source_folder) if f.endswith('.jpg')]

# 随机选择200张图片
selected_images = random.sample(image_files, 200)

# 复制选取的图片到目标文件夹
for image_name in selected_images:
    source_image_path = os.path.join(source_folder, image_name)
    # destination_image_path = os.path.join(destination_image_folder, image_name)
    shutil.move(source_image_path, destination_image_folder)

    # 获取对应的标签文件名
    label_filename = os.path.splitext(image_name)[0] + '.txt'
    source_label_path = os.path.join(label_folder, label_filename)
    # destination_label_path = os.path.join(destination_label_folder, label_filename)

    # 复制对应的标签文件到目标文件夹
    shutil.move(source_label_path, destination_label_folder)

print(f"随机选取了200张图片和对应的标签，已保存到目标文件夹：{destination_image_folder}\n,{destination_label_folder}")
