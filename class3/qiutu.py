import urllib.parse
import urllib.request
import re
import os
import time
def handle_request(url,page):
    url = url + str(page)+'/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36'
    }
    requset = urllib.request.Request(url=url,headers=headers)
    return requset
# <img src="//pic.qiushibaike.com/system/pictures/12165/121652338/medium/VGE8MIXQVWV2PUKL.jpg" alt="image">
def download_img(content,page):
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt=".*?">.*?</div>',re.S)#需要的内容是用.*括起来的，不用的话是用.*?
    ret = pattern.findall(content)
    # 遍历列表，依次下载图片
    i = 1
    for img_src in ret:
        # 生成链接
        img_src = 'https:'+img_src
        #生成文件夹，如果没有的话
        if not os.path.exists('class3/img'):
            os.mkdir('class3/img')
        # 发送请求下载文件
        filename = str(page)+'page_no'+str(i)+'.jpg'
        # filename = img_src.split('/')[-1]
        # 以最后的网站图片名作为名称
        filepath = 'class3/img' + '/' +filename
        urllib.request.urlretrieve(img_src, filepath)
        i=i+1

def main():
    url = 'https://www.qiushibaike.com/pic/page/'
    start_page = int(input('输入开始页码:'))
    end_page = int(input('输入结束代码:'))
    
    for page in range(start_page,end_page+1):
        print('第%s页开始下载'%page)
        # 生成请求对象
        request=handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        # 解析内容提取所有的图片链接，下载图片。
        download_img(content, page)
        print('第%s页下载完毕'%page)
        time.sleep(1)#停顿一下，防止频繁访问

if __name__ == '__main__':
    main()