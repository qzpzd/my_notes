import os
import shutil

# 定义文件夹路径
labels_folder = 'C:/Users\suso\Desktop/baidu\merege_red_labels'
images_folder = 'C:/Users\suso\Desktop/baidu\merege_red_images'
prefix = '20231023'

# 遍历 labels 文件夹中的所有 txt 文件
for filename in os.listdir(labels_folder):
    if filename.endswith('.txt'):
        # 构建源文件和目标文件的路径
        src_txt_path = os.path.join(labels_folder, filename)
        dst_txt_path = os.path.join(labels_folder, f'{prefix}_red_{filename[9:]}')

        # 添加前缀到标签文件
        os.rename(src_txt_path, dst_txt_path)

        # 找到对应的图像文件
        # image_filename = os.path.splitext(filename)[0] + '.jpg'
        # src_image_path = os.path.join(images_folder, image_filename)
        # dst_image_path = os.path.join(images_folder, f'{prefix}_red_{image_filename[9:]}')

        # # 添加前缀到图像文件
        # os.rename(src_image_path, dst_image_path)
