from PIL import Image
import os
import random

# 输入和输出文件夹路径
input_folder = "C:/Users\suso\Desktop\\baidu\\橙色"
output_folder = "C:/Users\suso\Desktop\\baidu\\resize_orange"

# 设置缩小的范围
min_width = 15  # 最小宽度
max_width = 50  # 最大宽度
min_height = 15  # 最小高度
max_height = 50 # 最大高度

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取输入文件夹中的所有图像文件
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# 循环处理每个图像文件
for image_file in image_files:
    input_path = os.path.join(input_folder, image_file)
    output_path = os.path.join(output_folder, image_file)

    # 打开图像文件
    image = Image.open(input_path)

    # 随机生成缩小后的宽度和高度
    new_width = random.randint(min_width, max_width)
    new_height = random.randint(min_height, max_height)

    # 将图像转换为RGB模式
    image = image.convert("RGB")

    # 调整图像大小
    resized_image = image.resize((new_width, new_height))

    # 保存缩小后的图像
    resized_image.save(output_path)

    print(f"缩小 {image_file} 完成")

print("所有图像处理完成")
