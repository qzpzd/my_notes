import os
import shutil

# 定义函数，参数分别为原始文件夹路径、目标文件夹路径、新的文件名前缀
def rename_files(src_folder, dest_folder, prefix):
    # 列出原始文件夹中的所有文件
    file_list = os.listdir(src_folder)

    # 遍历所有文件
    #count = 0
    for i, filename in enumerate(file_list):
        # 判断文件是否为图片
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
                        
            # 构造新文件名
            #new_filename = prefix + '_' + str(i) + os.path.splitext(filename)[1]
            new_filename = prefix + '_' + filename
            
            #print(new_filename)
            #exit()
            # 拼接原始文件路径和目标文件路径
            src_path = os.path.join(src_folder, filename)
            dest_path = os.path.join(dest_folder, new_filename)

            # 复制文件并重命名
            shutil.copy(src_path, dest_path)
            print(f"Rename {filename} to {new_filename}")
            #count += 1
def rename_all_files(src_folder, dest_folder, prefix):
    for root, dirs, file in os.walk(src_folder):
        for file_name in file:
            if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
                
                # 构造新文件名
                #new_filename = prefix + '_' + str(i) + os.path.splitext(filename)[1]
                new_filename = prefix + '_' + file_name
                
                #print(new_filename)
                #exit()
                # 拼接原始文件路径和目标文件路径
                src_path = os.path.join(root,file_name)
                dest_path = os.path.join(dest_folder, new_filename)
                # print(root,dirs,file)
                # exit()
                # 复制文件并重命名
                shutil.copy(src_path, dest_path)
                print(f"Rename {file_name} to {new_filename}")

# 调用函数，将原始文件夹中的所有图片文件复制到目标文件夹，并按照指定前缀和序号重命名
src_folder = '/home/disk/qizhongpei/projects/ultralytics/crop_imgs/20230526'
dest_folder = '/home/disk/qizhongpei/projects/datasets/phone128/train/hand_others'
prefix = 'hand_others_web_data_20230531' 	# 前缀应为hand_others_的字符串，也可以自定义。这是一个特

#rename_files(src_folder, dest_folder, prefix)
rename_all_files(src_folder, dest_folder, prefix)