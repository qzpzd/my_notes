import os

def delete_txt_files(image_dir, txt_dir):
    # 获取图片目录中的所有文件名
    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

    # 获取txt目录中的所有文件名
    txt_files = [f for f in os.listdir(txt_dir) if os.path.isfile(os.path.join(txt_dir, f))]

    # 遍历图片目录中的文件
    for image_file in image_files:
        # 构造对应的txt文件名
        txt_file = os.path.splitext(image_file)[0] + ".txt"

        # 检查txt文件是否存在于txt目录中
        if txt_file in txt_files:
            # 构造txt文件的完整路径
            txt_file_path = os.path.join(txt_dir, txt_file)

            # 删除txt文件
            os.remove(txt_file_path)
            print(f"Deleted: {txt_file_path}")

# 用法示例
image_directory = "C:/Users\Administrator\Desktop\error_image"
txt_directory = "C:/Users\Administrator\Desktop\yolo_pose_helmet\crop_helmet_labels"

delete_txt_files(image_directory, txt_directory)
