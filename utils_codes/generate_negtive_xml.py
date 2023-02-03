import cv2
import os
# '/home/disk/yenanfei/phoneData_padding/JPEGImages'
path = '/home/disk/qizhongpei/ssd_pytorch/OMS_phone/接打电话告警_video/上海_0928/'
xml_path = '/home/disk/qizhongpei/DMS_phone/PhoneDataset_recut_change/ImageSets/xml/上海_0928/'
Files = os.listdir(path)
for File in Files:
    headstr = """\
<annotation>
    <folder>VOC</folder>
    <filename>%s</filename>
    <source>
        <database>My Database</database>
    </source>
    <size>
        <width>%d</width>
        <height>%d</height>
        <depth>%d</depth>
    </size>
    <segmented>0</segmented>
</annotation>
            """
    name,exten = os.path.splitext(File)
    print(File)
    img = cv2.imread(path+File)
    height,width,_ = img.shape
    head=headstr % (name+'.jpg', width, height, 3)
    with open(xml_path+name+'.xml','w') as f:
        f.write(head)
