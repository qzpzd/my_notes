import os
import shutil

# 源图片目录
image_dir = "C:\\Users\\Administrator\\Desktop\\yolo_pose_helmet\\error_helmet\\images"

# txt文件目录
txt_dir = "C:\\Users\\Administrator\\Desktop\\yolo_pose_helmet\\crop_helmet_labels_1"

# 目标存储目录
labels_dir = "C:\\Users\\Administrator\\Desktop\\yolo_pose_helmet\\error_helmet\\labels"

# 获取图片目录中的所有文件名
image_files = os.listdir(image_dir)

# 遍历图片目录中的所有文件
for image_file in image_files:
    # 获取图片文件的文件名（不包含扩展名）
    image_filename = os.path.splitext(image_file)[0]

    # 构建对应的txt文件路径
    txt_file = os.path.join(txt_dir, image_filename + ".txt")

    # 如果txt文件存在则移动到新的目录
    if os.path.isfile(txt_file):
        shutil.move(txt_file, os.path.join(labels_dir, os.path.basename(txt_file)))
