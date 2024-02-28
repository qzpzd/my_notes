import cv2
import numpy as np
import os
import xml.etree.ElementTree as ET
from glob import glob

anno_dirs=glob('E:/Data/crowdhuman/Annotations_val/*.xml')

for anno_dir in anno_dirs:
    img_dir = anno_dir.replace('Annotations','JPEGImages').replace('xml','jpg')
    save_dir = anno_dir.replace('Annotations_val','JPEGImages').replace('xml','jpg')
    src = cv2.imread(img_dir)

    tree = ET.parse(anno_dir)
    root = tree.getroot()

    for obj in root.iter('object'):
        bbox = obj.find('bndbox')
        bbox = list(map(int, [bbox.find('xmin').text,
                            bbox.find('ymin').text,
                            bbox.find('xmax').text,
                            bbox.find('ymax').text]))

        cv2.rectangle(src,(bbox[0],bbox[1]),(bbox[2],bbox[3]),(0,255,255),2)
    cv2.imwrite(save_dir,src)
