import os
import glob

# 获取指定目录下所有图片文件的路径列表
image_directory = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet_head/select_large3/images/train'  # 替换为您的图片目录
txt_directory = '/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet_head/select_large3/labels/train'  # 替换为您的txt目录
image_files = glob.glob(os.path.join(image_directory, '*.[Jj][Pp][Gg]'))  # 如果还有其他格式，如png、bmp等，可以增加对应的glob模式
txt_files = glob.glob(os.path.join(txt_directory, '*.txt')) 
# 删除以VID_20230904_前缀的图片
for image_file in image_files:
    if image_file.startswith(os.path.join(image_directory, '2023_09_')):
        os.remove(image_file)
        # print(f"Deleted: {image_file}")

for txt_file in txt_files:
    if txt_file.startswith(os.path.join(txt_directory, '2023_09_')):
        os.remove(txt_file)
        # print(f"Deleted: {image_file}")