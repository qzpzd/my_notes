import os
import shutil

def copy_images(source_folder, destination_folder, num_copies):
    # 确保目标文件夹存在
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 获取源文件夹中的所有图片文件
    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # 遍历每个图片文件
    for image_file in image_files:
        source_path = os.path.join(source_folder, image_file)

        # 复制图片文件多次
        for i in range(num_copies):
            # 构造目标文件名，例如，如果源文件是"example.jpg"，目标文件可以是"example_copy_1.jpg"
            destination_file = f"{os.path.splitext(image_file)[0]}_copy_{i + 1}{os.path.splitext(image_file)[1]}"
            destination_path = os.path.join(destination_folder, destination_file)

            # 复制文件
            shutil.copy2(source_path, destination_path)

if __name__ == "__main__":
    # 设置源文件夹、目标文件夹和复制次数
    source_folder = "C:/Users\suso\Desktop\crop_head"
    destination_folder = "C:/Users\suso\Desktop\crop_head_copy"
    num_copies = 100

    # 执行复制操作
    copy_images(source_folder, destination_folder, num_copies)
