import os
import shutil
from sklearn.model_selection import train_test_split

# 读取数据集文件列表
data_path = '/home/disk/qizhongpei/projects/datasets/phone128/hand_others'
files = os.listdir(data_path)
files = [file for file in files if file.endswith('.jpg')]

# 划分数据集为训练集、验证集和测试集
train_files, val_test_files = train_test_split(files, test_size=0.2, random_state=42)
val_files, test_files = train_test_split(val_test_files, test_size=0.5, random_state=42)

# 创建文件夹并将文件移动到相应文件夹中
for file in train_files:
    src_file = os.path.join(data_path, file)
    dst_file = os.path.join('/home/disk/qizhongpei/projects/datasets/phone128/train/hand_others', file)
    shutil.copy(src_file, dst_file)

for file in val_files:
    src_file = os.path.join(data_path, file)
    dst_file = os.path.join('/home/disk/qizhongpei/projects/datasets/phone128/val/hand_others', file)
    shutil.copy(src_file, dst_file)

for file in test_files:
    src_file = os.path.join(data_path, file)
    dst_file = os.path.join('/home/disk/qizhongpei/projects/datasets/phone128/test/hand_others', file)
    shutil.copy(src_file, dst_file)
