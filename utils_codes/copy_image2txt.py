import os
import shutil

# 获取文件夹中所有的图片文件名
def get_image_files(folder):
    image_files = []
    for file in os.listdir(folder):
        if file.endswith(".jpg") or file.endswith(".png"):
            image_files.append(file)
    return image_files

# 将文件后缀改为txt格式
def change_extension(file, new_extension):
    file_name, _ = os.path.splitext(file)
    new_file = file_name + new_extension
    return new_file

# 判断文件是否存在于另一个文件夹中
def file_exists(file, folder):
    return os.path.exists(os.path.join(folder, file))

# 复制文件到新的文件夹中
def copy_file(file, source_folder, destination_folder):
    source_file = os.path.join(source_folder, file)
    destination_file = os.path.join(destination_folder, file)
    shutil.copyfile(source_file, destination_file)

# 主函数
def main():
    # 源文件夹和目标文件夹路径
    source_folder = "/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet/select/images/train"
    destination_folder = "/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet/large_labels/train"
    new_folder = "/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet/select/labels/train"
    # 获取源文件夹中的所有图片文件
    image_files = get_image_files(source_folder)

    # 遍历图片文件
    for file in image_files:
        # 将文件后缀改为txt格式
        new_file = change_extension(file, ".txt")

        # 判断文件是否存在于目标文件夹中
        if file_exists(new_file, destination_folder):
            # 复制文件到新的文件夹中
            copy_file(new_file, destination_folder, new_folder)

if __name__ == "__main__":
    main()
