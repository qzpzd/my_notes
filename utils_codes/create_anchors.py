import os
import numpy as np

save_txt = open('yolov5_helmet_priorbox.txt','w')

# anchor3 = [[13,21], [19,26], [14,37]]
# anchor2 = [[22,43], [28,66], [41,64]]
# anchor1 = [[35,92], [48,100], [64,133]]

anchor3 = [[10,13], [16,30], [33,23]]
anchor2 = [[30,61], [62,45], [59,119]]
anchor1 = [[116,90], [156,198], [373,326]]



for k in range(3):
    for j in range(16):
        for i in range(16):
            #line = '%.1f %.1f %.1f %.1f'%(i,j,anchor3[k][0],anchor3[k][1])
            save_txt.write(str(i*1.0)+'\n')
            save_txt.write(str(j*1.0)+'\n')
            save_txt.write(str(anchor3[k][0])+'\n')
            save_txt.write(str(anchor3[k][1])+'\n')
            save_txt.write(str(8.0)+'\n')

for k in range(3):
    for j in range(8):
        for i in range(8):
            #line = '%.1f %.1f %.1f %.1f'%(i,j,anchor2[k][0],anchor2[k][1])
            #save_txt.write(str(line)+'\n')
            save_txt.write(str(i*1.0)+'\n')
            save_txt.write(str(j*1.0)+'\n')
            save_txt.write(str(anchor2[k][0])+'\n')
            save_txt.write(str(anchor2[k][1])+'\n')
            save_txt.write(str(16.0)+'\n')

for k in range(3):
    for j in range(4):
        for i in range(4):
            #line = '%.1f %.1f %.1f %.1f'%(i,j,anchor1[k][0],anchor1[k][1])
            #save_txt.write(str(line)+'\n')
            save_txt.write(str(i*1.0)+'\n')
            save_txt.write(str(j*1.0)+'\n')
            save_txt.write(str(anchor1[k][0])+'\n')
            save_txt.write(str(anchor1[k][1])+'\n')
            save_txt.write(str(32.0)+'\n')
save_txt.close()
#
#
# def generate_anchor_txt(anchors, masks, img_size, strides):
#     anchor_txt = []
#     for mask in masks:
#         for idx in mask:
#             anchor = anchors[idx]
#             for stride in strides:
#                 x = anchor[0] / img_size[1] * stride
#                 y = anchor[1] / img_size[0] * stride
#                 w = anchor[0] / img_size[1] * stride
#                 h = anchor[1] / img_size[0] * stride
#                 scale = stride
#                 anchor_txt.append([x, y, w, h, scale])
#     return np.array(anchor_txt)
# def write_anchor_txt(anchor_txt, file_path):
#     with open(file_path, 'w') as file:
#         for anchor in anchor_txt:
#             line = ' '.join(str(x) for x in anchor)
#             file.write(line + '\n')
#
# if __name__ == '__main__':
#     anchors = [[10, 13], [16, 30], [33, 23], [30, 61], [62, 45], [59, 119], [116, 90], [156, 198], [373, 326]]
#     masks = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
#     img_size = (128, 128)
#     strides = [8, 16, 32]
#
#     anchor_txt = generate_anchor_txt(anchors, masks, img_size, strides)
#     file_path = "anchor.txt"
#     write_anchor_txt(anchor_txt, file_path)