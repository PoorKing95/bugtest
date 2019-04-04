#把励志中的标题和内容拿下来，保存到HTML文件中，标题用h1，内容使用P标签
import urllib.request
import urllib.parse
import re
import os

def create_request(url,page):
    '''这里是生成请求REQUEST'''
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36'
        }
    if page==None:
        request = urllib.request.Request(url=url,headers=headers)
    else:
        url = url+str(page)+'.html'
        request = urllib.request.Request(url=url,headers=headers)
    return request

def deal_text(wait_text):
    pattern_dad = re.compile(r'<ol class=" list-paddingleft-2" style="list-style-type: decimal;">(.*?)</ol>')
    pattern = re.compile(r'<li><p>(.*)</p><br/></li>')
    ret = pattern_dad.findall(wait_text)
    if ret:
        temp = ret[0].split('</p></li><li><p>')
        print(temp)
    else:
        print('没有值')

def download_inner(content,page):
    '''这里是打开，下载与写入处理'''
    pattern = re.compile(r'<h3><a href="(.*?)"><b>(.*?)</b></a></h3>')
    ret = pattern.findall(content)
    for herf_title in ret:
        a_herf = 'http://www.yikexun.cn'+herf_title[0]
        tittle = herf_title[-1]
        wait_url = create_request(a_herf,None)
        wait_text = urllib.request.urlopen(wait_url).read().decode()
        deal_text(wait_text)


def main():
    start_page = int(input('请输入开始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page,end_page+1):
        url = 'http://www.yikexun.cn/lizhi/qianming/list_50_'
        request = create_request(url,page)
        content = urllib.request.urlopen(request).read().decode()
        download_inner(content,page)


if __name__ == '__main__':
    main()