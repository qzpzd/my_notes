from http.client import IM_USED
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 指定中文字体，这里使用的是SimHei字体，你可以根据需要选择其他中文字体
font = FontProperties(fname=r"c:\windows/fonts\simsun.ttc", size=14)


def plot_image(title, src, dst):
    src = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
    dst = cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)
    plt.subplot(121),plt.imshow(src),plt.title('original')  
    plt.subplot(122),plt.imshow(dst),plt.title('enhanced') 
    plt.suptitle(title,fontproperties=font)
    plt.show()  

def cv_image(src, dst):
    cv2.namedWindow("src", cv2.WINDOW_NORMAL)
    cv2.namedWindow("dst", cv2.WINDOW_NORMAL)
    cv2.imshow("src", src)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#------------------------------------对比度增强------------------------------------
#直方图均衡化（灰度图）
def contrast_stretching(image_path):
    img = cv2.imread(image_path,0)
    min_val = np.min(img)
    max_val = np.max(img)
    out = ((img - min_val) / (max_val - min_val)) * 255
    return img,out.astype(np.uint8)

#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#直方图归一化
#灰度级主要在0~150之间，造成图像对比度较低，可用直方图归一化将图像灰度级拉伸到0~255,使其更清晰
def image_normalize(image_path):

    src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)
    dst = np.zeros_like(src)
    cv2.normalize(src, dst, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U) #公式

    #计算灰度直方图
    grayHist = cv2.calcHist([src], [0], None, [256], [0, 256])
    grayHist1 = cv2.calcHist([dst], [0], None, [256], [0, 256])
    #画出直方图
    x_range = range(256)
    plt.plot(x_range, grayHist, 'r', linewidth=1.5, c='black')
    plt.plot(x_range, grayHist1, 'r', linewidth=1.5, c='b')
    #设置坐标轴的范围
    y_maxValue = np.max(grayHist)
    plt.axis([0, 255, 0, y_maxValue]) #画图范围
    plt.xlabel("gray Level")
    plt.ylabel("number of pixels")
    plt.show()

    return src,dst
#-------------------------------------------------------------------

#-------------------------------------------------------------------
#彩色直方图均衡
def RGB_image(image_path):
    I = cv2.imread(image_path)
    
    b, g, r = cv2.split(I)
    
    b1 = cv2.equalizeHist(b)
    g1 = cv2.equalizeHist(g)
    r1 = cv2.equalizeHist(r)
    
    O = cv2.merge([b1,g1,r1])
    return I,O
#--------------------------------------------------------------

#--------------------------------------------------------------
#线性变换
#拉伸灰度级，提高对比度，压缩灰度级，降低对比度
def lineal_ehanced(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)#GRAYSCALE 
    #线性变换
    a = 2
    O = float(a) * img
    O[O>255] = 255 #大于255要截断为255
        
    #数据类型的转换
    O = np.round(O)
    O = O.astype(np.uint8)
    return img,O
#----------------------------------------------------------------------

#-----------------------------------------------------------------------
#自适应对比度增强（Adaptive Contrast Enhancement，ACE）
def getVarianceMean(scr, winSize):
    if scr is None or winSize is None:
        print("The input parameters of getVarianceMean Function error")
        return -1
    
    if winSize % 2 == 0:
        print("The window size should be singular")
        return -1 
    
    copyBorder_map=cv2.copyMakeBorder(scr,winSize//2,winSize//2,winSize//2,winSize//2,cv2.BORDER_REPLICATE)
    shape=np.shape(scr)
    
    local_mean=np.zeros_like(scr)
    local_std=np.zeros_like(scr)
    
    for i in range(shape[0]):
        for j in range(shape[1]):   
            temp=copyBorder_map[i:i+winSize,j:j+winSize]
            local_mean[i,j],local_std[i,j]=cv2.meanStdDev(temp)
            if local_std[i,j]<=0:
                local_std[i,j]=1e-8
            
    return local_mean,local_std
    
def adaptContrastEnhancement(image_path, winSize, maxCg):
    scr=cv2.imread(image_path)
    if scr is None or winSize is None or maxCg is None:
        print("The input parameters of ACE Function error")
        return -1
    
    YUV_img=cv2.cvtColor(scr,cv2.COLOR_BGR2YUV)    ##转换通道
    Y_Channel = YUV_img[:,:,0]
    shape=np.shape(Y_Channel)
    
    meansGlobal=cv2.mean(Y_Channel)[0]
    
    ##这里提供使用boxfilter 计算局部均质和方差的方法
    #    localMean_map=cv2.boxFilter(Y_Channel,-1,(winSize,winSize),normalize=True)
    #    localVar_map=cv2.boxFilter(np.multiply(Y_Channel,Y_Channel),-1,(winSize,winSize),normalize=True)-np.multiply(localMean_map,localMean_map)
    #    greater_Zero=localVar_map>0
    #    localVar_map=localVar_map*greater_Zero+1e-8
    #    localStd_map = np.sqrt(localVar_map)
   
    localMean_map, localStd_map=getVarianceMean(Y_Channel,winSize)

    for i in range(shape[0]):
        for j in range(shape[1]):
            
            cg = 0.2*meansGlobal/ localStd_map[i,j];
            if cg >maxCg:
                cg=maxCg
            elif cg<1:
                cg=1
            
            temp = Y_Channel[i,j].astype(float)
            temp=max(0,min(localMean_map[i,j]+cg*(temp-localMean_map[i,j]),255))
            
            #Y_Channel[i,j]=max(0,min(localMean_map[i,j]+cg*(Y_Channel[i,j]-localMean_map[i,j]),255))
            Y_Channel[i,j]=temp
                
            
    YUV_img[:,:,0]=Y_Channel
    
    dst=cv2.cvtColor(YUV_img,cv2.COLOR_YUV2BGR)
    
    return scr,dst
#--------------------------------------------------------------------
#调节图像饱和度，亮度与对比度
def adjust_saturation_brightness_contrast(image_path, saturation_factor, brightness_factor, contrast_factor):
    image = cv2.imread(image_path)
    # 调整饱和度
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * saturation_factor, 0, 255)

    # 调整亮度
    bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    modified_image = np.clip(bgr_image * brightness_factor, 0, 255)

    # 调整对比度
    modified_image = np.clip((modified_image - 128) * contrast_factor + 128, 0, 255)

    # 保存修改后的图像
    cv2.imwrite(image_path, modified_image.astype(np.uint8))

    return image,modified_image.astype(np.uint8)
#------------------------------------------------------------------------------------

def main():
    if not os.path.exists(image_path):
        print("The file name error,please check it")
        return -1

    # #直方图均衡化（灰度图）
    # img,dstimg = contrast_stretching(image_path)#或者img_enhanced = cv2.equalizeHist(img)
    # plot_image('直方图均衡化（灰度图）',img, dstimg)
    # #直方图均衡化（彩色图）
    # img,dstimg = RGB_image(image_path)
    # plot_image('直方图均衡化（彩色图）',img, dstimg)
    # #直方图归一化
    # img,dstimg = image_normalize(image_path)
    # plot_image('直方图归一化',img, dstimg)
    # #线性变换
    # img,dstimg = lineal_ehanced(image_path)
    # plot_image('线性变换',img, dstimg)
    # #自适应释放图
    # img,dstimg=adaptContrastEnhancement(image_path,15,10)
    # plot_image('自适应释放图',img, dstimg)
    # # cv_image(img, dstimg)

    # 调整参数：饱和度、亮度、对比度
    saturation_factor = 1.5  # 增加饱和度
    brightness_factor = 1.2  # 增加亮度
    contrast_factor = 1.3    # 增加对比度
    img,dstimg = adjust_saturation_brightness_contrast(image_path, saturation_factor, brightness_factor, contrast_factor)
    # plot_image('综合调整',img, dstimg)

    return 0
 
if __name__ =="__main__":
    for image_name in os.listdir('F:\Download/fire detection.v3-set.yolov5pytorch/train/region_image'): 

        # image_path='C:/Users/suso/Desktop/frame_167_jpg.rf.e7c882acaf0ff6759f838391ba4f9301_class0.jpg'
        image_path = 'F:\Download/fire detection.v3-set.yolov5pytorch/train/region_image/' + image_name
        main()
