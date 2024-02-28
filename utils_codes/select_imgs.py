# import os
# import random
# import shutil



# def get_path():
#     global path
#     path = os.path.dirname(os.path.abspath(__file__))
   
# def get_file_path(path,file_name):
#     return os.path.join(path, file_name)

# def get_file_name(file_name):
#     return os.path.splitext(file_name)[0]

# def get_img_list(path):
#     imglist = []
#     for img in os.listdir(path):
#         if img.endswith(".jpg"):
#             imgpath = get_file_path(path,img)
#             imglist.append(imgpath)
#     print("oldnum: ", len(imglist))
#     imglist = list(set(imglist))
#     print("newnum: ", len(imglist))

# def move_images(src_folder, dest_folder):
#     # 获取源文件夹中的所有文件
#     file_list = os.listdir(src_folder)
#     move_list = []
#     for filename in file_list:
#         # 判断文件是否是图片文件
#         if filename.endswith('.jpg')  and filename[-6:-5] !="_":
#             # 构造源文件路径和目标文件路径
#             src_path = os.path.join(src_folder, filename)
#             dest_path = os.path.join(dest_folder, filename)
#             move_list.append(src_path)
#             # 移动文件
#             shutil.move(src_path, dest_path)
#             #print(f"Moved {src_path} to {dest_path}")
#     print(f"Moved {len(move_list)} images")


# def select_images(src_folder, dest_folder, num_images):
#     # 获取源文件夹中的所有图片文件
#     image_files = [f for f in os.listdir(src_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
#     # 随机选择num_images个文件
#     selected_files = random.sample(image_files, num_images)
#     # 复制选中的文件到目标文件夹中
#     for filename in selected_files:
#         src_path = os.path.join(src_folder, filename)
#         dest_path = os.path.join(dest_folder, filename)
#         shutil.move(src_path, dest_path)
#         #print(f"Copied {src_path} to {dest_path}")
#     print(f"{len(selected_files)} to {dest_folder}")
    
# def select_images1(src_folder, src_folder1, src_folder2, dest_folder):
#     # 获取源文件夹中的所有图片文件
#     image_files = [f for f in os.listdir(src_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
#     # 随机选择num_images个文件
#     image_files1 = [f for f in os.listdir(src_folder1) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

#     image_files2 = [f for f in os.listdir(src_folder2) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
#     # 复制选中的文件到目标文件夹中
#     for filename in image_files:
#         if filename not in image_files1 and not in image_files2:
#             src_path = os.path.join(src_folder, filename)
#             dest_path = os.path.join(dest_folder, filename)
#             shutil.move(src_path, dest_path)
#             #print(f"Copied {src_path} to {dest_path}")

# def remove_images(src_folder, dest_folder):
#     # 获取源文件夹中的所有图片文件
#     image_files = [f for f in os.listdir(src_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
#     # 随机选择num_images个文件
#     image_files1 = [f for f in os.listdir(dest_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
#     num = len(image_files)
#     # 复制选中的文件到目标文件夹中
#     for filename in image_files1:
#         if filename  in image_files:
#             src_path = os.path.join(src_folder, filename)
#             os.remove(src_path) 
#             image_files.remove(filename)
#     print(f"remove {num - len(image_files)} from {src_folder}" )
    

# if __name__ == '__main__':

#     src_folder = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/images/train"
#     src_folder1 = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/positive_samples"
#     src_folder2 = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/negative_samples"
#     dest_folder = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/other_samples"

#     if not os.path.exists(src_folder):
#         print("Folder does not exist")
#     if not os.path.exists(dest_folder):
#         os.makedirs(dest_folder)
    
#     #get_img_list(src_folder)

#     # 调用函数，将源文件夹中的所有图片文件移动到目标文件夹中
#     #move_images(src_folder, dest_folder)
#     # 调用函数，从源文件夹中随机选择n个图片文件，复制到目标文件夹中
#     #select_images(src_folder, dest_folder, 300)
#     #调用函数，从源文件将一部分图片与另一个文件夹下不同的图片移动到其它文件夹下
#     select_images1(src_folder, src_folder1,src_folder2, dest_folder)

#     # remove_images(src_folder, dest_folder)


'''
利用python循环遍历一个images/train目录中所有图像，如果该图像不在另外两个目录中，
则复制图像与包含其对应文件名的目录labels/train中的的txt文件分别复制到新的两个目录中
'''
# import os
# import shutil

# # 指定images/train目录的路径
# train_dir = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data"
# # 指定另外两个目录的路径，用于存储图像和标签
# positive_samples_dir = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/positive_samples"
# negative_samples_dir = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/negative_samples"

# # 指定用于保存新图像和标签的目录
# new_images_dir = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/other_samples/images"
# new_labels_dir = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/other_samples/labels"
# os.makedirs(new_images_dir, exist_ok=True)
# os.makedirs(new_labels_dir, exist_ok=True)

# # 获取images/train目录中的所有图像文件名
# image_files = os.listdir(train_dir + "/images/train")

# # 遍历images/train目录中的图像文件
# for image_file in image_files:
#     image_path = os.path.join(train_dir, "images/train", image_file)
#     label_path = os.path.join(train_dir, "labels/train", os.path.splitext(image_file)[0] + '.txt')

#     # 检查图像是否同时存在于另外两个目录中，如果不存在，则复制到新目录
#     if not (os.path.exists(os.path.join(positive_samples_dir, image_file)) or os.path.exists(os.path.join(negative_samples_dir, image_file))):
#         # 复制图像到新目录
#         shutil.copy(image_path, os.path.join(new_images_dir, image_file))
#         # 复制标签文件到新目录
#         shutil.copy(label_path, os.path.join(new_labels_dir, os.path.basename(label_path)))


'''
利用python分别将多个目录中的图像与txt文件进行分离，分别放到对应目录下的images与labels目录中
'''
# import os
# import shutil

# # 指定多个源目录的路径
# source_directories = [
#     "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/0.001_negative_samples",
#     # "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/negative_samples",
#     # 添加更多源目录...
# ]

# # 指定用于保存分离后图像和标签的目标目录
# # target_dir = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/"
# # os.makedirs(target_dir, exist_ok=True)

# for source_dir in source_directories:
#     # 创建目标目录中的子目录，分别用于存放图像和标签
#     target_images_dir = os.path.join(source_dir, "images")
#     target_labels_dir = os.path.join(source_dir, "labels")
#     os.makedirs(target_images_dir, exist_ok=True)
#     os.makedirs(target_labels_dir, exist_ok=True)

#     # 遍历源目录中的文件
#     for root, dirs, files in os.walk(source_dir):
#         for file in files:
#             if file.endswith('.jpg'):
#                 # 如果是图像文件，复制到images目录
#                 image_path = os.path.join(root, file)
#                 shutil.move(image_path, os.path.join(target_images_dir, file))
                
#                 # 寻找相应的标签文件（假设标签文件与图像文件同名，只是扩展名不同）
#                 label_file = os.path.splitext(file)[0] + '.txt'
#                 label_path = os.path.join(root, label_file)
                
#                 # 如果找到标签文件，复制到labels目录
#                 if os.path.exists(label_path):
#                     shutil.move(label_path, os.path.join(target_labels_dir, label_file))

# # 所有图像和标签已经分离并存放在对应的images和labels目录中


'''
利用python遍历一个目录中images/train中所有图像包括jpg与png图像，
如果该图像文件同时存在于第二个目录中且不存在第三个目录中则删除该图像与labels/train目录中与该图像对应文件名的txt文件，
'''
import os

# 指定images/train目录的路径
train_image_dir = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/images/train"
# 指定第二个目录的路径
second_dir = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/select_pos"
# 指定第三个目录的路径
third_dir = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/0.001_negative_samples/images"
# 指定labels/train目录的路径
train_label_dir = "/home/disk/qizhongpei/projects/yolov5/fire/data/new_fire_data/labels/train"

# 获取第二个目录中的所有文件名
second_files = os.listdir(second_dir)
# 获取第三个目录中的所有文件名
third_files = os.listdir(third_dir)

# 遍历images/train目录中的图像文件
i = 0
for root, dirs, files in os.walk(train_image_dir):
    for image_file in files:
        if image_file.lower().endswith(('.jpg', '.png')):
            image_path = os.path.join(root, image_file)
            label_file = os.path.splitext(image_file)[0] + '.txt'
            label_path = os.path.join(train_label_dir, label_file)
            
            # 检查图像文件是否同时存在于第二个目录中且不存在于第三个目录中
            if image_file in second_files and image_file not in third_files:
                print(image_file)
                # 检查标签文件是否存在
                if os.path.exists(label_path):
                    # 删除标签文件
                    os.remove(label_path)
                # 删除图像文件
                os.remove(image_path)
                i+=1
            
print(f"共删除 {i} 个文件")
'''
从训练集中选择正负样本分别放在两个目录中
'''
# import os
# import shutil

# # 指定 YOLOv5 训练集的目录路径
# train_dir = "path/to/your/train/directory"
# # 指定用于保存正样本的目录
# positive_samples_dir = "path/to/positive_samples"
# # 指定用于保存负样本的目录
# negative_samples_dir = "path/to/negative_samples"
# os.makedirs(positive_samples_dir, exist_ok=True)
# os.makedirs(negative_samples_dir, exist_ok=True)

# # 遍历训练集目录中的图像文件
# for root, dirs, files in os.walk(os.path.join(train_dir, "images")):
#     for file in files:
#         if file.endswith('.jpg'):
#             image_path = os.path.join(root, file)
#             label_path = os.path.join(train_dir, "labels", os.path.splitext(file)[0] + '.txt')

#             # 判断标签文件是否存在目标对象
#             with open(label_path, 'r') as label_file:
#                 has_object = any(line.strip() for line in label_file)

#             if has_object:
#                 # 复制正样本的图像和标签到保存正样本的目录
#                 shutil.copy(image_path, os.path.join(positive_samples_dir, file))
#                 shutil.copy(label_path, os.path.join(positive_samples_dir, os.path.basename(label_path)))
#             else:
#                 # 复制负样本的图像和标签到保存负样本的目录
#                 shutil.copy(image_path, os.path.join(negative_samples_dir, file))
#                 shutil.copy(label_path, os.path.join(negative_samples_dir, os.path.basename(label_path))
