import urllib.request
url = 'https://movie.douban.com'
#自定义请求头
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36',
    'Referer':'https://movie.douban.com/',
    'Connection':'keep-alive'
}
req = urllib.request.Request(url,headers=headers)
temp = urllib.request.urlopen(req)
html = temp.read().decode('utf-8')
print('下载成功')
f = open('test1.txt','w',encoding='utf8')
f.write(html)
f.close()