import os
import random
import shutil

def split_files(image_folder, txt_folder, images_train_folder, images_val_folder, labels_train_folder, labels_val_folder, split_ratio):
    # 创建train和val文件夹
    os.makedirs(images_train_folder, exist_ok=True)
    os.makedirs(images_val_folder, exist_ok=True)
    os.makedirs(labels_train_folder, exist_ok=True)
    os.makedirs(labels_val_folder, exist_ok=True)

    # 获取image_folder中的所有图片文件
    image_files = [file for file in os.listdir(image_folder) if file.endswith('.jpg') or file.endswith('.png')]

    # 获取txt_folder中的所有txt文件
    txt_files = [file for file in os.listdir(txt_folder) if file.endswith('.txt')]

    # 计算划分的数量
    num_train = int(len(image_files) * split_ratio)

    # 随机选择train文件
    train_files = random.sample(image_files, num_train)

    # 将train文件复制到train文件夹中
    for file in train_files:
        src_image = os.path.join(image_folder, file)
        src_txt = os.path.join(txt_folder, file.replace('.jpg', '.txt').replace('.png', '.txt'))
        dst_image = os.path.join(images_train_folder, file)
        dst_txt = os.path.join(labels_train_folder, file.replace('.jpg', '.txt').replace('.png', '.txt'))
        shutil.copy(src_image, dst_image)
        shutil.copy(src_txt, dst_txt)

    # 将剩余的文件复制到val文件夹中
    for file in image_files:
        if file not in train_files:
            src_image = os.path.join(image_folder, file)
            src_txt = os.path.join(txt_folder, file.replace('.jpg', '.txt').replace('.png', '.txt'))
            dst_image = os.path.join(images_val_folder, file)
            dst_txt = os.path.join(labels_val_folder, file.replace('.jpg', '.txt').replace('.png', '.txt'))
            shutil.copy(src_image, dst_image)
            shutil.copy(src_txt, dst_txt)

# 设置源文件夹和目标文件夹的路径
image_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/YOLOv5-Tools/CrowHuman2YOLO/data/crowdhuman/crop_images/select_from_10000/'  # 图片文件夹的路径
txt_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/YOLOv5-Tools/CrowHuman2YOLO/data/crowdhuman/crop_labels/select_from_10000'  # txt文件夹的路径
images_train_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet_head/select_large1/images/select_train'  # train文件夹的路径
images_val_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet_head/select_large1/images/select_val'  # val文件夹的路径
labels_train_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet_head/select_large1/labels/select_train'  # train文件夹的路径
labels_val_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet_head/select_large1/labels/select_val'  # val文件夹的路径

# 设置划分比例
split_ratio = 0.7  # 70%的文件复制到train文件夹，30%的文件复制到val文件夹

# 调用函数进行文件划分和复制
split_files(image_folder, txt_folder, images_train_folder, images_val_folder, labels_train_folder, labels_val_folder, split_ratio)
