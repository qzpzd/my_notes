from PIL import Image
import os
import random

def crop_and_save_images(input_folder, output_folder, num_crops_per_image):
    # 获取图片文件夹中的所有图片文件
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

    for idx, image_file in enumerate(image_files):
        # 读取图片
        image_path = os.path.join(input_folder, image_file)
        original_image = Image.open(image_path)

        for crop_num in range(num_crops_per_image):
            # 随机生成截取的正方形大小
            size = random.randint(50, 90)
            left = random.randint(0, original_image.width - size)
            top = random.randint(0, original_image.height - size)

            # 截取图片
            cropped_image = original_image.crop((left, top, left + size, top + size))

            # 保存截取后的图片
            output_filename = f"negative_20231218_crop_{size}_{idx}_{crop_num}.jpg"
            output_path = os.path.join(output_folder, output_filename)
            cropped_image.save(output_path)

if __name__ == "__main__":
    input_folder = "C:/Users\suso\Desktop/black_crop"
    output_folder = "C:/Users\suso\Desktop/black_crop_result"
    num_crops_per_image = 3  # 设置每张图片截取的个数

    crop_and_save_images(input_folder, output_folder, num_crops_per_image)
