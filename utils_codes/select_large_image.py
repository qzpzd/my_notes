import os
import random
import shutil

def filter_images(img_source_folder, label_source_folder, target_folder, txt_folder, num_images):
    # 创建目标文件夹和txt文件夹
    os.makedirs(target_folder, exist_ok=True)
    os.makedirs(txt_folder, exist_ok=True)

    # 获取源文件夹中的所有文件
    files = os.listdir(img_source_folder)

    # 随机选择num_images张图像
    random_images = random.sample(files, num_images)

    for image in random_images:
        image_path = os.path.join(img_source_folder, image)

        # 使用OpenCV或其他库读取图像的长宽
        # 这里使用示例代码，需要安装OpenCV库
        import cv2
        img = cv2.imread(image_path)
        height, width, _ = img.shape

        if height > 40 and width > 40:
            # 复制图像到目标文件夹
            target_path = os.path.join(target_folder, image)
            shutil.copy(image_path, target_path)

            # 生成对应的txt文件名
            txt_filename = os.path.splitext(image)[0] + '.txt'
            label_path = os.path.join(label_source_folder, txt_filename)
            txt_path = os.path.join(txt_folder, txt_filename)

            # 复制txt到目标文件夹
            shutil.copy(label_path, txt_path)


# 示例文件夹路径和参数
# img_source_folder = './crowdhuman/crop_images/train/'
# label_source_folder = './crowdhuman/crop_labels/new_train/'

# img_source_folder = './crowdhuman/crop_images/large_val/'
# label_source_folder = './crowdhuman/crop_labels/large_val/'
# target_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/YOLOv5-Tools/CrowHuman2YOLO/data/crowdhuman/crop_images/large_val_3100/'
# txt_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/YOLOv5-Tools/CrowHuman2YOLO/data/crowdhuman/crop_labels/large_val_3100/'

img_source_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet/images/test/'
label_source_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet/labels/test/'
target_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet/large_images/test/'
txt_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet/large_labels/test/'

num_images = 1878

# 筛选图像并保存
filter_images(img_source_folder, label_source_folder, target_folder, txt_folder, num_images)
