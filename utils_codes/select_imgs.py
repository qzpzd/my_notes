import os
import random
import shutil



def get_path():
    global path
    path = os.path.dirname(os.path.abspath(__file__))
   
def get_file_path(path,file_name):
    return os.path.join(path, file_name)

def get_file_name(file_name):
    return os.path.splitext(file_name)[0]

def get_img_list(path):
    imglist = []
    for img in os.listdir(path):
        if img.endswith(".jpg"):
            imgpath = get_file_path(path,img)
            imglist.append(imgpath)
    print("oldnum: ", len(imglist))
    imglist = list(set(imglist))
    print("newnum: ", len(imglist))

def move_images(src_folder, dest_folder):
    # 获取源文件夹中的所有文件
    file_list = os.listdir(src_folder)
    move_list = []
    for filename in file_list:
        # 判断文件是否是图片文件
        if filename.endswith('.jpg')  and filename[-6:-5] !="_":
            # 构造源文件路径和目标文件路径
            src_path = os.path.join(src_folder, filename)
            dest_path = os.path.join(dest_folder, filename)
            move_list.append(src_path)
            # 移动文件
            shutil.move(src_path, dest_path)
            #print(f"Moved {src_path} to {dest_path}")
    print(f"Moved {len(move_list)} images")


def select_images(src_folder, dest_folder, num_images):
    # 获取源文件夹中的所有图片文件
    image_files = [f for f in os.listdir(src_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
    # 随机选择num_images个文件
    selected_files = random.sample(image_files, num_images)
    # 复制选中的文件到目标文件夹中
    for filename in selected_files:
        src_path = os.path.join(src_folder, filename)
        dest_path = os.path.join(dest_folder, filename)
        shutil.move(src_path, dest_path)
        #print(f"Copied {src_path} to {dest_path}")
    print(f"{len(selected_files)} to {dest_folder}")
    
def select_images1(src_folder, src_folder1, dest_folder):
    # 获取源文件夹中的所有图片文件
    image_files = [f for f in os.listdir(src_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
    # 随机选择num_images个文件
    image_files1 = [f for f in os.listdir(src_folder1) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
    # 复制选中的文件到目标文件夹中
    for filename in image_files:
        if filename not in image_files1:
            src_path = os.path.join(src_folder, filename)
            dest_path = os.path.join(dest_folder, filename)
            shutil.move(src_path, dest_path)
            #print(f"Copied {src_path} to {dest_path}")

def remove_images(src_folder, dest_folder):
    # 获取源文件夹中的所有图片文件
    image_files = [f for f in os.listdir(src_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
    # 随机选择num_images个文件
    image_files1 = [f for f in os.listdir(dest_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
    num = len(image_files)
    # 复制选中的文件到目标文件夹中
    for filename in image_files1:
        if filename  in image_files:
            src_path = os.path.join(src_folder, filename)
            os.remove(src_path) 
            image_files.remove(filename)
    print(f"remove {num - len(image_files)} from {src_folder}" )

if __name__ == '__main__':

    src_folder = "/home/disk/qizhongpei/projects/datasets/phone128/test/no_hand_phone"
    src_folder1 = "D:\\mybook\\datasets\\play_phone_data\\原始数据\\crop_imgs\\筛选后图像\\hand_others_crop_select\\val"
    dest_folder = "/home/disk/qizhongpei/projects/datasets/phone128/none_img"

    if not os.path.exists(src_folder):
        print("Folder does not exist")
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    #get_img_list(src_folder)

    # 调用函数，将源文件夹中的所有图片文件移动到目标文件夹中
    #move_images(src_folder, dest_folder)
    # 调用函数，从源文件夹中随机选择n个图片文件，复制到目标文件夹中
    #select_images(src_folder, dest_folder, 300)
    #调用函数，从源文件将一部分图片与另一个文件夹下不同的图片移动到其它文件夹下
    #select_images1(src_folder, src_folder1, dest_folder)

    remove_images(src_folder, dest_folder)