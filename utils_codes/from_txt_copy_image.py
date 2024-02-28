import os
import shutil

# 设置图像文件夹、文本文件夹和目标文件夹的路径
image_folder = "F:\Download/fire detection.v3-set.yolov5pytorch/train\images"
text_folder = "F:\Download/fire detection.v3-set.yolov5pytorch/train\select_labels"
output_folder = "F:\Download/fire detection.v3-set.yolov5pytorch/train\select_images"

# 获取图像文件夹中的文件名
image_files = os.listdir(image_folder)
# 获取文本文件夹中的文件名
text_files = os.listdir(text_folder)

# 提取图像文件和文本文件的基本文件名（不包括扩展名）
image_filenames = [os.path.splitext(file)[0] for file in image_files]
text_filenames = [os.path.splitext(file)[0] for file in text_files]

# 检查哪些文本文件对应的基本文件名在图像文件夹中存在
matching_filenames = set(image_filenames).intersection(text_filenames)

# 创建目标文件夹，如果不存在的话
os.makedirs(output_folder, exist_ok=True)

# 复制匹配的图像文件到目标文件夹
for filename in matching_filenames:
    image_file = os.path.join(image_folder, filename + ".jpg")  # 假设图像文件扩展名为.jpg
    if os.path.exists(image_file):
        shutil.copy(image_file, output_folder)

# 打印复制完成的消息
print(f"复制了 {len(matching_filenames)} 张图像到目标文件夹。")
