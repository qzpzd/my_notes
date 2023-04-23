# import re  #为了正则表达式
# import requests#请求网页url
# import os #操作系统
# import time #时间

# num=0    #给图片名字加数字
# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
#         'Cookie':'BDIMGISLOGIN=0; winWH=%5E6_898x979; BDqhfp=%E7%8E%A9%E6%89%8B%E6%9C%BA%E5%9B%BE%E7%89%87%26%26NaN-1undefined%26%262448%26%265; BIDUPSID=9D30E42392637B80F7E84A192DEE24B8; PSTM=1621996580; __yjs_duid=1_0a42e9ba207c21b706403d92b0eefbfd1621997932458; BAIDUID=DF822A35618F36F387CC1A47B050D866:FG=1; BDUSS=o0TUYwY0xRTC14ODJHejBIZjNHZURqM29xY0ZNZmpUc3NTbWNjY241cDNCbGxqSVFBQUFBJCQAAAAAAAAAAAEAAABtB90pxu7W0MXgMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHd5MWN3eTFjMH; BDUSS_BFESS=o0TUYwY0xRTC14ODJHejBIZjNHZURqM29xY0ZNZmpUc3NTbWNjY241cDNCbGxqSVFBQUFBJCQAAAAAAAAAAAEAAABtB90pxu7W0MXgMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHd5MWN3eTFjMH; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDSFRCVID=6wCOJeC62igsvpQjpbXeJ7Zjj8nON8RTH6aoftZ8CQsVR8WQNhzmEG0P2x8g0KA-FxRqogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tR4J_I8yfIt3fP36q4jh5PLt5xrea4RXHD7yWCkKbhOcOR5Jj65EbntBKbQBbPjv5mLfhJc_fnrc8Cn-3MA--t4E5bCO3hoeQHuO-Mjk2PcVsq0x055We-bQyPLL0JvN-COMahv15h7xOM5sQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_Jj8eJJ6P; cleanHistoryStatus=0; BA_HECTOR=8125258l2kaka4818g2h0hfu1i00hdp1m; BAIDUID_BFESS=DF822A35618F36F387CC1A47B050D866:FG=1; BDSFRCVID_BFESS=6wCOJeC62igsvpQjpbXeJ7Zjj8nON8RTH6aoftZ8CQsVR8WQNhzmEG0P2x8g0KA-FxRqogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tR4J_I8yfIt3fP36q4jh5PLt5xrea4RXHD7yWCkKbhOcOR5Jj65EbntBKbQBbPjv5mLfhJc_fnrc8Cn-3MA--t4E5bCO3hoeQHuO-Mjk2PcVsq0x055We-bQyPLL0JvN-COMahv15h7xOM5sQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_Jj8eJJ6P; ZFY=DZNOVps56pdqIJL:ACP013:BQ53fy51BQGIziQnzY:AS:Aw:C; delPer=0; PSINO=6; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[Tp5-T0kH1pb]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; indexPageSugList=%5B%22%E9%A9%BE%E9%A9%B6%E5%91%98%E7%8E%A9%E6%89%8B%E6%9C%BA%22%2C%22%E6%89%8B%E6%9C%BA%E6%8B%BF%E7%94%B5%E8%AF%9D%E5%9B%BE%E7%89%87%22%2C%22%E6%89%8B%E5%9B%BE%E7%89%87%22%2C%22%E6%89%8B%E6%9C%BA%E7%94%B5%E8%AF%9D%E5%9B%BE%E7%89%87%22%2C%22%E6%89%8B%E6%9C%BA%E5%9B%BE%E7%89%87%22%2C%22%E7%94%B5%E8%AF%9D%E5%9B%BE%E7%89%87%22%2C%22%E6%89%8B%E6%8A%B1%E5%90%8E%E8%84%91%E5%8B%BA%E5%9B%BE%E7%89%87%22%2C%22%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E5%8F%91%E5%B1%95%E5%8E%86%E7%A8%8B%E5%9B%BE%E7%89%87%22%2C%22%E6%B1%BD%E8%BD%A6%E5%86%85%E6%89%93%E7%94%B5%E8%AF%9D%E5%9B%BE%E7%89%87%22%5D; ab_sr=1.0.1_NmVjMDZlNTY3YTI3NDk0N2RjMjFkYzA5ZDQ4ZmI1MDdkZTQ0ZjM3ZmJjZDZjZjRhOWI2YjA2ZDc4MWYwZDliZjRlZGRkYWM5NGNkZmQ0OTVhZjNhY2FmN2M4NWNlYjI0MGY0Yjc1MWQ0Y2YyMmExZWM0YjE4ODRmZDkyM2FjNzY5YTdhYzM0NGIxNGFkMDQ2NjdjZTE3ZWY4MTlkZWY3Ng==',#这里需要大家根据自己的浏览器情况自行填写
#         'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
#         'Accept-Encoding':'gzip, deflate, br',
#         'Accept-Language':'zh-CN,zh;q=0.9',
#         'connection':'close'

#         }  #请求头，谷歌浏览器里面有，具体在哪里找到详见我上一条csdn博客
# #图片页面的url
# url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1677741098896_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=&ie=utf-8&sid=&word=%E9%A9%BE%E9%A9%B6%E5%91%98%E7%8E%A9%E6%89%8B%E6%9C%BA'

# #通过requests库请求到了页面
# html=requests.get(url,headers=header)
# #防止乱码
# html.encoding='utf8'
# #打印页面出来看看
# print(html.text)
 
# html=html.text
# pachong_picture_path='C:\\Users\\suso\\Desktop\\hand_phone'
# if not os.path.exists(pachong_picture_path):
#     os.mkdir(pachong_picture_path)
 
 
 
# res=re.findall('"hoverURL":"(.*?)"',html)  #正则表达式，筛选出html页面中符合条件的图片源代码地址url
# for i in res:   #遍历
#     num=num+1       #数字加1，这样图片名字就不会重复了
#     time.sleep(8)
#     picture=requests.get(i)       #得到每一张图片的大图
#     file_name='C:\\Users\\suso\\Desktop\\hand_phone\\hand_phone_'+str(num)+".jpg"   #给下载下来的图片命名。加数字，是为了名字不重复
#     f=open(file_name,"wb")    #以二进制写入的方式打开图片
#     f.write(picture.content)   # 往图片里写入爬下来的图片内容，content是写入内容的意思
 
#     print(i)    #看看有哪些url
# f.close()      #结束f文件操作


# import requests#爬虫库
# import re#正则表达式库
# import os#系统库
# import time#时间库

# headers = {#文件头，必须有，否则会安全验证
#         "Accept":"application/json, text/javascript, */*; q=0.01",
#         'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Connection': 'keep-alive',
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
#         'Host': 'image.baidu.com',
#         'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=&st=-1&fm=result&fr=&sf=1&fmq=1610952036123_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E6%98%9F%E9%99%85',
#         'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'X-Requested-With': 'XMLHttpRequest'
#     }

# url='http://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word='#百度链接
# print("@非常道")
# keyword=input("请输入图片关键词：")
# filename=input("请输入图片文件名：")
# # keyword='cyberpunk'
# countmax=eval(input("请输入要爬取的图片数量："))
# url=url+keyword+"&pn="
# time_start=time.time()#获取初始时间

# strhtml=requests.get(url,headers=headers)#get方式获取数据
# string=str(strhtml.text)
# # with open("data.txt","w",encoding='utf-8') as f:#这个编码是个问题
# #     f.write(string)  #这句话自带文件关闭功能，不需要再写f.close()
# # print("已爬取，数据存入data.txt")

# #正则表达式取得图片总数量
# totalnum = re.findall('<div id="resultInfo" style="font-size: 13px;">(.*?)</div>', string) 
# print("百度图片"+totalnum[0])

# img_url_regex = '"thumbURL":"(.*?)",'#正则匹配式
# count=0#总共下载的图片数
# index=0#链接后面的序号
# page=0#当前搜集的页
# while(1):
#     strhtml=requests.get(url+str(index),headers=headers)#get方式获取数据
#     string=str(strhtml.text)
#     print("已爬取网页")
#     pic_url = re.findall(img_url_regex, string)  # 先利用正则表达式找到图片url
#     print("第"+str(page+1)+"页共收集到"+str(len(pic_url))+"张图片")
#     index+=len(pic_url)#网址索引向后，跳到下一页继续搜刮图片
#     try:#如果没有文件夹就创建
#         os.mkdir('.'+r'\\' + filename)
#     except:
#         pass
    
#     for each in pic_url:
#         print('正在下载第' + str(count + 1) + '张图片，图片地址:' + str(each))
#         try:
#             if each is not None:
#                 pic = requests.get(each, timeout=5)
#             else:
#                 continue
#         except BaseException:
#             print('错误，当前图片无法下载')
#             continue
#         else:
#             string = '.' + r'\\' + filename + r'\\' + filename + '_' + str(count+1) + '.jpg'
#             fp = open(string, 'wb')
#             fp.write(pic.content)
#             fp.close()
#             count += 1
#         if countmax==count:
#                 break    
#     if countmax==count:
#                 break
# time_end=time.time()#获取结束时间
# print('处理完毕，共耗时:'+str(time_end-time_start)+"秒")
# input("@非常道 按任意键继续")

#下载谷歌图片
#aim:爬取google图片

# from selenium import webdriver
# import time
# from lxml import etree
# import random
# from urllib import request
# import os
 
# def pic_url_get(num):
#     for i in range(num):
#         time.sleep(random.uniform(0,2))
#         content = driver.page_source
#         html = etree.HTML(content)
#         pic_url = html.xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img/@src')[0]
#         pic_urls.append(pic_url)
#         print('第{}张图片获取成功'.format(i+1))
#         next_page_button = driver.find_element_by_xpath('//div[@id="Sva75c"]/div/div/div[3]/div[2]//div/div[1]/div[1]/div[1]/a[3]')
#         next_page_button.click()
 
# def pics_download():
#     a = 1
#     for pic_url in pic_urls:
#         opener = request.build_opener()
#         opener.addheaders = [('User-agent',
#                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'),
#                              ('accept',
#                               'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')]
#         request.install_opener(opener)
#         name = os.path.split(pic_url)[-1]
#         if '.' not in name:
#             name = name + '.jpg'
#         try:
#             request.urlretrieve(pic_url, r'C:\\Users\\suso\\Desktop\\google\\{0}'.format(name))
#             print(name + '下载完成！！！')
#         except:
#             request.urlretrieve(pic_url, r'C:\\Users\\suso\\Desktop\\google\\{0}.jpg'.format(a))
#             print(str(a) + '下载完成！！！')
#             a+=1
# if __name__ =='__main__':
#     if os.path.isdir(r'C:\\Users\\suso\\Desktop\\Google'): #修改成你想要存储到的地方
#         pass
#     else:
#         os.mkdir(r'C:\\Users\\suso\\Desktop\\Google') #修改成你想要存储到的地方
#     num = int(input('请输入你想要下载的图片数量(整数)：'))
#     pic_urls = []
#     url = input('请输入你想要下载的谷歌图片网址：')
#     driver_path = r'C:\\Users\\suso\Desktop\\chromedriver' #修改成你的chromedriver的路径
#     driver = webdriver.Chrome(executable_path=driver_path)
#     driver.get(url)
#     first_pic_button = driver.find_element_by_xpath('//div[@id="islrg"]/div[1]/div[1]/a[1]')
#     first_pic_button.click()
#     pic_url_get(num)
#     print(pic_urls)
#     pics_download()
#     print('-----------------------------------爬取完成------------------------------------------')

# from icrawler.builtin import BaiduImageCrawler
# from icrawler.builtin import BingImageCrawler
# from icrawler.builtin import GoogleImageCrawler
# #需要爬取的关键字
# list_word = ['车内手机']
# for word in list_word:
#     #bing爬虫
#     #保存路径
#     # bing_storage = {'root_dir':'photo\\'+word}#photo为主文件名，可以修改为别的名称，，列表有多少个，我们就在主列表产生
#     # #从上到下依次是解析器线程数，下载线程数，还有上面设置的保存路径
#     # bing_crawler = BingImageCrawler(parser_threads=4,
#     #                                 downloader_threads=8,
#     #                                 storage=bing_storage)
#     # #开始爬虫，关键字+图片数量
#     # bing_crawler.crawl(keyword=word,
#     #                   max_num=200)

#     #百度爬虫
#     # baidu_storage = {'root_dir': 'baidu\\' + word}
#     # baidu_crawler = BaiduImageCrawler(parser_threads=2,
#     #                                   downloader_threads=4,
#     #                                   storage=baidu_storage)
#     # baidu_crawler.crawl(keyword=word,
#     #                     max_num=2000)


#     # google爬虫
#     google_storage = {'root_dir': 'google' + word}
#     google_crawler = GoogleImageCrawler(parser_threads=4,
#                                        downloader_threads=4,
#                                        storage=google_storage)
#     google_crawler.crawl(keyword=word,
#                         max_num=200)
    
import os
import sys
import time
import urllib
import requests
import re
from bs4 import BeautifulSoup
import time
 
header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'
}
url = "https://cn.bing.com/images/async?q={0}&first={1}&count={2}&scenario=ImageBasicHover&datsrc=N_I&layout=ColumnBased&mmasync=1&dgState=c*9_y*2226s2180s2072s2043s2292s2295s2079s2203s2094_i*71_w*198&IG=0D6AD6CBAF43430EA716510A4754C951&SFX={3}&iid=images.5599"
 
 
def getImage(url, count):
    '''从原图url中将原图保存到本地'''
    try:
        time.sleep(0.5)
        urllib.request.urlretrieve(url, './google/' + str(count + 1) + '.jpg')
    except Exception as e:
        time.sleep(1)
        print("本张图片获取异常，跳过...")
    else:
        print("图片+1,成功保存 " + str(count + 1) + " 张图")
 
 
def findImgUrlFromHtml(html, rule, url, key, first, loadNum, sfx, count):
    '''从缩略图列表页中找到原图的url，并返回这一页的图片数量'''
    soup = BeautifulSoup(html, "lxml")
    link_list = soup.find_all("a", class_="iusc")
    url = []
    for link in link_list:
        result = re.search(rule, str(link))
        #将字符串"amp;"删除
        url = result.group(0)
        #组装完整url
        url = url[8:len(url)]
        #打开高清图片网址
        getImage(url, count)
        count += 1
    #完成一页，继续加载下一页
    return count
 
 
def getStartHtml(url, key, first, loadNum, sfx):
    '''获取缩略图列表页'''
    page = urllib.request.Request(url.format(key, first, loadNum, sfx),
                                  headers=header)
    html = urllib.request.urlopen(page)
    return html
 
 
if __name__ == '__main__':
    name = "手机"    #图片关键词
    path = './google/'   #图片保存路径
    countNum = 600  #爬取数量
    key = urllib.parse.quote(name)
    first = 1
    loadNum = 35
    sfx = 1
    count = 0
    rule = re.compile(r"\"murl\"\:\"http\S[^\"]+")
    if not os.path.exists(path):
        os.makedirs(path)
    while count < countNum:
        html = getStartHtml(url, key, first, loadNum, sfx)
        count = findImgUrlFromHtml(html, rule, url, key, first, loadNum, sfx,
                                   count)
        first = count + 1
        sfx += 1