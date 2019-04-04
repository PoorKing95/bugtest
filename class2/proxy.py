import urllib.request
import urllib.parse

handler = urllib.request.ProxyHandler({
    'http':'127.0.0.1:1080'
})
opener = urllib.request.build_opener(handler)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36'
}
url = 'https://www.baidu.com/s?ie=UTF-8&wd=IP'
request = urllib.request.Request(url, headers=headers)
response = opener.open(request)
with open('class2/ip.html','wb')as fp:
    fp.write(response.read())