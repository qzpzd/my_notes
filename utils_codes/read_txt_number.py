import os
import re
from collections import defaultdict

def count_classes_in_txt_files(directory):
    class_counts = defaultdict(int)
    txt_files = [f for f in os.listdir(directory) if f.endswith(".txt")]

    for txt_file in txt_files:
        file_path = os.path.join(directory, txt_file)
        with open(file_path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            # 假设 YOLOv5 格式的标注行为 "class_index x_center y_center width height"
            match = re.match(r"(\d+)", line)
            if match:
                class_index = int(match.group(1))
                class_counts[class_index] += 1

    return class_counts

if __name__ == "__main__":
    directory_path = "/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet_head/select_large3/labels/train"  # 替换成你的数据集目录
    class_counts = count_classes_in_txt_files(directory_path)

    # 打印每个类别的数目
    for class_index, count in class_counts.items():
        print(f"Class {class_index}: {count} instances")

    # 打印总的类别数目
    total_classes = len(class_counts)
    print(f"Total Classes: {total_classes}")
