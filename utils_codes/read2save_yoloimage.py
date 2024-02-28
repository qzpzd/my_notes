import cv2
import os

# 定义数据集文件夹的路径
dataset_images = 'F:\Download/fire detection.v3-set.yolov5pytorch/train\select_images'
dataset_labels = 'F:\Download/fire detection.v3-set.yolov5pytorch/train\select_labels'

# 遍历数据集文件夹中的所有文件
for file_name in os.listdir(dataset_images):
    if file_name.endswith('.jpg'):
        # 读取图像
        image_path = os.path.join(dataset_images, file_name)
        image = cv2.imread(image_path)
        
        # 读取对应的标签文件
        label_file = os.path.splitext(file_name)[0] + '.txt'
        label_file_path = os.path.join(dataset_labels, label_file)
        
        # 读取标签文件内容
        with open(label_file_path, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            # 解析Yolo标签数据
            parts = line.strip().split()
            class_id = int(parts[0])
            x_center, y_center, width, height = map(float, parts[1:])
            
            # 计算目标区域的左上角和右下角坐标
            x1 = int((x_center - width / 2) * image.shape[1])
            y1 = int((y_center - height / 2) * image.shape[0])
            x2 = int((x_center + width / 2) * image.shape[1])
            y2 = int((y_center + height / 2) * image.shape[0])
            
            # 提取目标区域
            target_region = image[y1:y2, x1:x2]
            
            # 可视化标注目标区域
            # cv2.imshow('Target Region', target_region)
            # cv2.waitKey(0)
            
            # 保存标注目标区域图像
            output_folder = 'F:\Download/fire detection.v3-set.yolov5pytorch/train/region_image'
            os.makedirs(output_folder, exist_ok=True)
            output_file_name = os.path.splitext(file_name)[0] + f'_class{class_id}.jpg'
            output_file_path = os.path.join(output_folder, output_file_name)
            cv2.imwrite(output_file_path, target_region)
            
cv2.destroyAllWindows()
