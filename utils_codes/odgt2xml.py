import json
import os
import xml.etree.ElementTree as ET
import cv2

def pretty_xml(element, indent, newline, level=0):              # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
    if element:                                                 # 判断element是否有子元素    
        if (element.text is None) or element.text.isspace():    # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
            # else:                                             # 此处两行如果把注释去掉，Element的text也会另起一行
            # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element)                                        # 将element转成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):            # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
            subelement.tail = newline + indent * (level + 1)
        else:                                                   # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个    
            subelement.tail = newline + indent * level
        pretty_xml(subelement, indent, newline, level=level + 1)# 对子元素进行递归操作

def write_xml(img_name,filepath,labeldicts,h,w,d):               #参数imagename是图片名（无后缀）
    root = ET.Element('annotation')                             #创建Annotation根节点
    ET.SubElement(root,'folder').text = 'JPEGImages'            #创建folder子节点（无后缀）        
    ET.SubElement(root, 'filename').text = str(img_name)         #创建filename子节点（无后缀）
    sizes = ET.SubElement(root,'size')                          #创建size子节点            
    ET.SubElement(sizes, 'width').text = str(w)                 #没带脑子直接写了原图片的尺寸......
    ET.SubElement(sizes, 'height').text = str(h)
    ET.SubElement(sizes, 'depth').text = str(d)
    for labeldict in labeldicts:
        objects = ET.SubElement(root, 'object')                 #创建object子节点                                                                     
        ET.SubElement(objects, 'name').text = str(labeldict['name'])
        bndbox = ET.SubElement(objects,'bndbox')
        ET.SubElement(bndbox, 'xmin').text = str(int(labeldict['xmin']))
        ET.SubElement(bndbox, 'ymin').text = str(int(labeldict['ymin']))
        ET.SubElement(bndbox, 'xmax').text = str(int(labeldict['xmax']))
        ET.SubElement(bndbox, 'ymax').text = str(int(labeldict['ymax']))
    tree = ET.ElementTree(root)
    pretty_xml(root, '\t', '\n')
    tree.write(filepath, encoding='utf-8')
    
f = open('annotation_train.odgt','r')
img_dir = './JPEGImages_train/'
xml_dir = './Annotations_train/'

lines = f.readlines()
for line in lines:
    labeldicts = []
    img_boxes = []
    
    data = json.loads(line)
    ID = data['ID']
    print(ID)
    
    #new_ID = ID.replace(',','')   
    img_path = img_dir + ID + '.jpg'   
    img = cv2.imread(img_path)
    h,w,d = img.shape    
    
    xml_path = xml_dir + ID + '.xml'
    #os.rename(img_path,img_dir + new_ID + '.jpg')
    gtboxes = data['gtboxes']
    for i in range(len(gtboxes)):
        print(gtboxes[i])
        tag = gtboxes[i]['tag']
        extra = gtboxes[i]['extra']
        head_attr = gtboxes[i]['head_attr']
              
        if 'mask' in tag:
            continue       
        if 'ignore' in extra:
            ignore = int(extra['ignore'])
            if ignore == 1:
                continue
        elif 'unsure' in extra:
            unsure = int(extra['unsure'])
            if unsure == 1:
                continue
        else:
            ignore = int(head_attr['ignore'])
            unsure = int(head_attr['unsure'])
            #occ = int(head_attr['occ'])
            if ignore == 1 or unsure == 1:# or occ == 1:
                continue

        hbox = gtboxes[i]['hbox']
        img_boxes.append(hbox)
    
    for j in range(len(img_boxes)):
        img_box = img_boxes[j]
        xmin = float(img_box[0])
        ymin = float(img_box[1])
        xmax = float(img_box[0] + img_box[2])
        ymax = float(img_box[1] + img_box[3])
        
        new_dict = {'name': 'head',
                    'xmin': xmin, 
                    'ymin': ymin,
                    'xmax': xmax,
                    'ymax': ymax
                    }
        labeldicts.append(new_dict)         
    write_xml(ID, xml_path, labeldicts,h,w,d) 
