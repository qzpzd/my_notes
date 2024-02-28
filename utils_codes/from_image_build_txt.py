import os
import shutil

# 源文件夹和目标文件夹的路径
source_folder = 'F:/数据集/fire/baidu/frame_image_1_crop'  # 替换为包含图片的源文件夹路径
target_folder = 'F:/数据集/fire/baidu/frame_image_1_crop_txt'  # 目标文件夹路径，用于存放txt文件

# 前缀
prefix = '20230913'

# 获取源文件夹中的所有图片文件
image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

# 遍历图片文件并重命名
for image_file in image_files:
    # # 构建新的文件名，添加前缀
    # new_name = f"{prefix}_{image_file}"
    
    # # 重命名图片文件
    # source_path = os.path.join(source_folder, image_file)
    # target_path = os.path.join(source_folder, new_name)
    # os.rename(source_path, target_path)
    
    # 生成对应的txt文件到labels文件夹
    new_label_name = os.path.splitext(image_file)[0]
    txt_file_path = os.path.join(target_folder, f"{new_label_name}.txt")
    with open(txt_file_path, 'w') as txt_file:
        txt_file.write('')  # 写入空文本

print("重命名和生成txt文件完成。")

# import os
# import shutil

# # 源文件夹和目标文件夹路径
# source_folder = 'F:\Download/fire_fuyangben\error_images'
# destination_folder = 'F:\Download/fire_fuyangben\error_images'

# # 遍历源文件夹中的所有文件
# for filename in os.listdir(source_folder):
#     # 检查文件是否是图片文件（可以根据您的需求添加更多的文件类型）
#     if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
#         source_file_path = os.path.join(source_folder, filename)
        
#         # 复制文件40次
#         for i in range(40):
#             # 构造新文件名，例如：original_filename_1.jpg, original_filename_2.jpg, ...
#             base_name, ext = os.path.splitext(filename)
#             new_filename = f"{base_name}_copy_{i + 1}{ext}"
            
#             # 目标文件路径
#             destination_file_path = os.path.join(destination_folder, new_filename)
            
#             # 复制文件
#             shutil.copy2(source_file_path, destination_file_path)

# print("复制完成")
