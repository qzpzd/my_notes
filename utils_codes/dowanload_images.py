# import requests
# from bs4 import BeautifulSoup
# import os
# import base64
# from io import BytesIO

# def download_images(query, num_images, save_directory):
#     # 创建保存图片的文件夹
#     os.makedirs(save_directory, exist_ok=True)

#     # 构建搜索URL
#     search_url = f"https://www.bing.com/images/search?q={query}&count={num_images}"
#     headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'}
#     # 发送HTTP请求并获取响应
#     response = requests.get(search_url, headers=headers)
#     response.raise_for_status()
#     # print(response.text)
#     # 使用BeautifulSoup解析响应内容
#     soup = BeautifulSoup(response.text, "html.parser")
#     # soup = BeautifulSoup(response.text, 'lxml')

#     # 查找所有图片链接
#     image_links = soup.find_all("a", class_="iusc")

#     # 下载并保存图片
#     for i, link in enumerate(image_links):
#         if i >= num_images:
#             break

#         # 获取图片URL
#         try:
#             image_url = link.find("img")["src"]
#             print(link.find("img"))
#         except:
#             image_url = link.find("img")['data-src']
#             # print(link.find("img"))
#         # print(image_url)
#         if image_url[0:4]=='data':
#             # 切割字符串，获取后面图片数据部分
#             image_data = image_url.split(',')[1]
#             # 解码-->二进制数据
#             image = base64.b64decode(image_data)
#             with open(os.path.join(save_directory, f"image{i+1}.jpg"), "wb") as f:
#                 f.write(bytes(image))

#         else:

#             # 发送HTTP请求并保存图片
#             image_response = requests.get(image_url)
#             image_response.raise_for_status()
            
#             # 保存图片到本地文件夹
#             with open(os.path.join(save_directory, f"image{i+1}.jpg"), "wb") as f:
#                 f.write(image_response.content)

#         print(f"下载图片 {i+1}/{num_images} 完成")

#     print("所有图片下载完成！")


# query = "黑色,灰色背景图片70*70"  # 搜索关键字
# num_images = 500 # 要下载的图片数量
# save_directory = "C:/Users/suso/Desktop/bing/black_crop/"  # 保存图片的文件夹路径

# download_images(query, num_images, save_directory)


# import base64
# from PIL import Image
# from io import BytesIO

# base64_str="data:image/jpeg;base64,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"

# head,context=base64_str.split(",")  # 将base64_str以“,”分割为两部分
# img_data = base64.b64decode(context)    # 解码时只要内容部分

# image = Image.open(BytesIO(img_data))
# image.show()

from icrawler.builtin import BaiduImageCrawler 
from icrawler.builtin import BingImageCrawler 
from icrawler.builtin import GoogleImageCrawler 
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.3f} seconds to execute.")
        return result
    return wrapper
@timer
def my_data_processing_function():
    n = 1
    for i in range(100):
        n*=i+1
    return n
result = my_data_processing_function()
print(result)

# #需要爬虫的关键字
# # list_word = ['抽烟 行人','吸烟 行人','接电话 行人','打电话 行人', '玩手机 行人']
list_word = ['黑色,灰色背景图片70*70']
for word in list_word:
    # bing爬虫
    # 保存路径
    bing_storage = {'root_dir': 'C:\\Users\\suso\\Desktop\\bing\\'+"black_crop"}
    #从上到下依次是解析器线程数，下载线程数，还有上面设置的保存路径
    bing_crawler = BingImageCrawler(parser_threads=2,
                                    downloader_threads=4,
                                    storage=bing_storage)
    #开始爬虫，关键字+图片数量
    bing_crawler.crawl(keyword=word,
                       max_num=500)

    # #百度爬虫
    # baidu_storage = {'root_dir': 'C:\\Users\\suso\\Desktop\\baidu\\' + word}
    # baidu_crawler = BaiduImageCrawler(parser_threads=2,
    #                                   downloader_threads=4,
    #                                   storage=baidu_storage)
    # baidu_crawler.crawl(keyword=word,
    #                     max_num=2000)


#     # google爬虫
#     google_storage = {'root_dir': 'C:\\Users\\suso\\Desktop\\google\\' + word}
#     google_crawler = GoogleImageCrawler(parser_threads=4,
#                                        downloader_threads=4,
#                                        storage=google_storage)
#     google_crawler.crawl(keyword=word,
#                          max_num=2000)


# # -*- coding: UTF-8 -*-"""
# import requests
# import tqdm


# def configs(search, page, number):
#     """

#     :param search:
#     :param page:
#     :param number:
#     :return:
#     """
#     url = 'https://image.baidu.com/search/acjson'
#     params = {
#         "tn": "resultjson_com",
#         "logid": "11555092689241190059",
#         "ipn": "rj",
#         "ct": "201326592",
#         "is": "",
#         "fp": "result",
#         "queryWord": search,
#         "cl": "2",
#         "lm": "-1",
#         "ie": "utf-8",
#         "oe": "utf-8",
#         "adpicid": "",
#         "st": "-1",
#         "z": "",
#         "ic": "0",
#         "hd": "",
#         "latest": "",
#         "copyright": "",
#         "word": search,
#         "s": "",
#         "se": "",
#         "tab": "",
#         "width": "",
#         "height": "",
#         "face": "0",
#         "istype": "2",
#         "qc": "",
#         "nc": "1",
#         "fr": "",
#         "expermode": "",
#         "force": "",
#         "pn": str(60 * page),
#         "rn": number,
#         "gsm": "1e",
#         "1617626956685": ""
#     }
#     return url, params


# def loadpic(number, page):
#     """

#     :param number:
#     :param page:
#     :return:
#     """
#     while (True):
#         if number == 0:
#             break
#         url, params = configs(search, page, number)
#         result = requests.get(url, headers=header, params=params).json()
#         url_list = []
#         for data in result['data'][:-1]:
#             url_list.append(data['thumbURL'])
#         for i in range(len(url_list)):
#             getImg(url_list[i], 60 * page + i, path)
#             bar.update(1)
#             number -= 1
#             if number == 0:
#                 break
#         page += 1
#     print("\nfinish!")


# def getImg(url, idx, path):
#     """

#     :param url:
#     :param idx:
#     :param path:
#     :return:
#     """
#     img = requests.get(url, headers=header)
#     file = open(path + 'black_crop_' + str(idx + 1) + '.jpg', 'wb')
#     file.write(img.content)
#     file.close()


# if __name__ == '__main__':
#     search = input("请输入搜索内容：")
#     number = int(input("请输入需求数量："))
#     path = 'C:\\Users\\suso\\Desktop\\baidu\\black_crop\\'
#     header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

#     bar = tqdm.tqdm(total=number)
#     page = 0
#     loadpic(number, page)


