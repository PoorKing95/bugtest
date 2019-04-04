import urllib.request
url1 = 'http://www.baidu.com'
response=urllib.request.urlopen(url1)
#encode() 字符串转换二进制
#decode() 二进制转化字符串
print(dict(response.getheaders()))
# with open('baidu.html','w',encoding='utf8') as fp:
#     fp.write(response.read().decode('utf8'))
#read()是读取，是字节类型的
#geturl()根据响应的内容，获取请求的URL
#getheaders() 获取头部信息
#readlines() 获取状态码,按行读取，都是字节类型
with open('baidu1.html','wb') as fp:
    fp.write(response.read())