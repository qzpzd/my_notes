import os

def count_empty_txt_files(directory):
    empty_files_count = 0
    txt_files = [f for f in os.listdir(directory) if f.endswith(".txt")]

    for txt_file in txt_files:
        file_path = os.path.join(directory, txt_file)
        if os.path.getsize(file_path) == 0:
            empty_files_count += 1

    return empty_files_count

if __name__ == "__main__":
    directory_path = "/home/disk/qizhongpei/projects/my_project/Smart_Construction/alldata/helmet_head/select_large1/labels/train"  # 替换成你的数据集目录
    empty_files_count = count_empty_txt_files(directory_path)

    print(f"Total Empty .txt Files: {empty_files_count}")
