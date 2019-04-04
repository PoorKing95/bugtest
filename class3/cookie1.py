#模拟登陆豆瓣
import urllib.request
import urllib.parse
import http.cookiejar

#创建一个cookiejar对象
cj = http.cookiejar.CookieJar()
#通过cookiejar创建一个handler
handler = urllib.request.HTTPCookieProcessor(cj)
#根据handler创建一个opener
opener = urllib.request.build_opener(handler)

url = 'https://accounts.douban.com/j/mobile/login/basic'
username = input('请输入用户名:')
password = input('请输入密码:')
formdata = {
    'ck':'',
    'name':username,
    'password':password,
    'remember':'false',
    'ticket':''
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    
}
formdata = urllib.parse.urlencode(formdata).encode()
request = urllib.request.Request(url=url,headers = headers)
response = opener.open(request,data = formdata)
print(response.read().decode())
get_url = 'https://www.douban.com/people/193580875/'
request = urllib.request.Request(url=get_url,headers=headers)
response = opener.open(request)
with open('class3/cookie/my.html','wb')as fp:
    fp.write(response.read())
