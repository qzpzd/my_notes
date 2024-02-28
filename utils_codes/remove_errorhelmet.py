import os
import shutil

def delete_images_and_labels(folder_path, image_source_folder, label_source_folder):
    image_n = 0
    label_n = 0
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否是以".jpg"或".png"结尾
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # 删除图像文件
            file_path = os.path.join(image_source_folder, filename)
            if os.path.exists(file_path):
                os.remove(file_path)
                image_n += 1
            # 删除对应的txt文件
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            label_path = os.path.join(label_source_folder, txt_filename)
            if os.path.exists(label_path):
                os.remove(label_path)
                label_n += 1
    print(f'remove:{image_n} images  and  {label_n} labels')

# 指定文件夹路径
folder_path = "/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/head/select/errorhead"
image_source_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/head/select/images/train'
label_source_folder = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/head/select/labels/train'
# 调用函数删除图像文件和对应的txt文件
delete_images_and_labels(folder_path, image_source_folder, label_source_folder)
