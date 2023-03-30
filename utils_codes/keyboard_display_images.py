import sys,tty,os,termios
from PIL import Image
import cv2

# 定义图片文件夹路径和图片文件列表
folder = '/home/disk/qizhongpei/projects/datasets/phone128/rm_img/val'
images = os.listdir(folder)
current_image = 0

# 定义函数显示当前图片
def show_image():
    img = cv2.imread(os.path.join(folder, images[current_image]))
    cv2.imshow("img",img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    # img = Image.open(os.path.join(folder, images[current_image]))
    # img.show()
    # img.close()
  

# 显示第一张图片
show_image()
def getkey():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    try:
        while True:
            b = os.read(sys.stdin.fileno(), 3).decode()
            
            if len(b) == 3:
                k = ord(b[2])
            else:
                k = ord(b)
            print(k)
            key_mapping = {
                127: 'backspace',
                10: 'return',
                32: 'space',
                9: 'tab',
                27: 'esc',
                65: 'up',
                66: 'down',
                67: 'right',
                68: 'left',
                51: 'delete'
                
                

            }
            return key_mapping.get(k, chr(k))
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
try:
    # while True:
    #     k = getkey()
    #     if k == 'esc':
    #         quit()
    #     else:
    #         print(k)

    # 监听键盘事件
    while True:
        k = getkey()
        if k == 'esc':
            quit()
        elif k =='left':
            # 左箭头键，显示上一张图片
            current_image -= 1
            if current_image < 0:
                current_image = len(images) - 1
            show_image()
        elif k =='right':
            # 右箭头键，显示下一张图片
            current_image += 1
            if current_image >= len(images):
                current_image = 0
            show_image()
        elif k =='delete':
            # 删除键，删除当前图片
            os.remove(os.path.join(folder, images[current_image]))
            images.pop(current_image)
            if current_image >= len(images):
                current_image = 0
            show_image()
        else:
            print(k)

except (KeyboardInterrupt, SystemExit):
    os.system('stty sane')
    print('stopping.')