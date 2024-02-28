import os

# 定义文件夹路径
folder_path = 'F:\Download/linshi'

# 遍历文件夹中的所有 txt 文件
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        # 打开文件以读取和写入
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # 处理每一行，将第一个数字改为 0
        for i in range(len(lines)):
            line = lines[i].strip()  # 去除行末尾的换行符和空白字符
            parts = line.split()     # 分割行为单词
            if len(parts) > 0 and parts[0].isdigit():
                if parts[0]=='2':
                    parts[0] = '0'       # 将第一个数字改为 0
                    lines[i] = ' '.join(parts) + '\n'
                else:
                    lines[i] = ''

        # 写入修改后的内容回到文件中
        with open(file_path, 'w') as file:
            file.writelines(lines)
