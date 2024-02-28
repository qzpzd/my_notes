import os

def replace_first_char_in_yolov5_txt(directory):
    # 遍历指定目录及其子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件是否为.txt结尾且位于当前层级（如果你只想处理当前目录下的文件，取消注释下面这行）
            # if file.endswith('.txt') and root == directory:
            if file.endswith('.txt'):
                filepath = os.path.join(root, file)
                
                # 打开文件并读取所有行
                with open(filepath, 'r') as f:
                    lines = f.readlines()

                # 创建一个新的列表存储修改后的行
                new_lines = []
                for line in lines:
                    # 分割每行数据，假设每行的第一个元素前没有空格
                    parts = line.split()
                    
                    # 检查是否符合Yolov5格式（通常第一列是类别ID，后面跟的是框坐标）
                    if len(parts) > 4:  # 假设至少有类别ID和4个坐标值
                        # 将第一个字符由'0'替换为'1'
                        modified_line = parts[0].replace('1', '0') + ' ' + ' '.join(parts[1:])
                        new_lines.append(modified_line)
                    else:
                        new_lines.append(line)  # 不符合格式的行保持不变

                # 写回修改后的行到原文件
                with open(filepath, 'w') as f:
                    f.writelines(new_lines)

# 调用函数，传入你要处理的目录路径
replace_first_char_in_yolov5_txt('./error_head/labels')