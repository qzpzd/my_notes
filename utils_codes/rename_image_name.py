import os

# 输入文件夹路径，包含图片文件
input_folder = "C:/Users\suso\Desktop/baidu/frame_image_1"

# 获取文件夹中的所有图片文件
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# 重命名图片文件
for i, image_file in enumerate(image_files):
    # 构造新的文件名，可以根据需要定义命名规则
    new_name = f"20231023_image_{i + 1}.jpg"  # 例如，以"image_1.jpg"、"image_2.jpg"等方式重命名

    # 构建原始文件路径和新文件路径
    old_path = os.path.join(input_folder, image_file)
    new_path = os.path.join(input_folder, new_name)

    # 重命名文件
    os.rename(old_path, new_path)

    print(f"重命名 {image_file} 为 {new_name}")

print("所有图片重命名完成")
