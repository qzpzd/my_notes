# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # 读取YOLO格式的标签文件
# def read_yolo_label(label_path):
#     with open(label_path, 'r') as file:
#         lines = file.readlines()
#     labels = []
#     for line in lines:
#         parts = line.strip().split()
#         if len(parts) == 5:
#             labels.append(parts)
#     return labels

# # 读取图像文件并绘制边界框以及标签
# def visualize_image(image_path, labels, class_names):
#     image = cv2.imread(image_path)
#     for label in labels:
#         class_id, x_center, y_center, width, height = map(float, label)
#         x_min = int((x_center - width / 2) * image.shape[1])
#         y_min = int((y_center - height / 2) * image.shape[0])
#         x_max = int((x_center + width / 2) * image.shape[1])
#         y_max = int((y_center + height / 2) * image.shape[0])

#         cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        
#         class_name = class_names[int(class_id)]
#         label_text = f'{class_name}'
#         cv2.putText(image, label_text, (x_min, y_min - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

#     plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#     plt.axis('off')
#     plt.show()

# # 图像和标签路径
# image_path = 'path_to_image.jpg'
# label_path = 'path_to_label.txt'

# # 类别名称列表，根据你的数据集自行定义
# class_names = ['Cooking Oil', 'Electrical', 'Gas', 'Liquid', 'Metal', 'Solid']

# # 读取标签文件
# labels = read_yolo_label(label_path)

# # 可视化图像和边界框，包括标签
# visualize_image(image_path, labels, class_names)

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取YOLO格式的标签文件
def read_yolo_label(label_path):
    with open(label_path, 'r') as file:
        lines = file.readlines()
    labels = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 5:
            labels.append(parts)
    return labels

# 读取图像文件并绘制边界框以及标签
def visualize_images_in_folder(image_folder, label_folder, class_names):
    for image_filename in os.listdir(image_folder):
        if image_filename.endswith('.jpg'):
            image_path = os.path.join(image_folder, image_filename)
            label_filename = os.path.splitext(image_filename)[0] + '.txt'
            label_path = os.path.join(label_folder, label_filename)

            if os.path.isfile(label_path):
                labels = read_yolo_label(label_path)

                image = cv2.imread(image_path)
                for label in labels:
                    class_id, x_center, y_center, width, height = map(float, label)
                    x_min = int((x_center - width / 2) * image.shape[1])
                    y_min = int((y_center - height / 2) * image.shape[0])
                    x_max = int((x_center + width / 2) * image.shape[1])
                    y_max = int((y_center + height / 2) * image.shape[0])

                    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

                    class_name = class_names[int(class_id)]
                    label_text = f'{class_name}'
                    cv2.putText(image, label_text, (x_min, y_min - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()

# 图像和标签文件夹路径
image_folder = 'C:/Users\Administrator\Desktop\yolo_pose_helmet\error_helmet\images'
label_folder = 'C:/Users\Administrator\Desktop\yolo_pose_helmet\error_helmet\labels'

# 类别名称列表，根据你的数据集自行定义
# class_names = ['Cooking Oil', 'Electrical', 'Gas', 'Liquid', 'Metal', 'Solid']
# class_names = ['0', '1', '2', '3', '4']
class_names = ['0','1']

# 可视化文件夹中的图像和边界框，包括标签
visualize_images_in_folder(image_folder, label_folder, class_names)
