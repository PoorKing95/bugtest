import urllib.request
import urllib.parse
#进行user-agent的伪装
#构建请求对象 urllib.request.Request()
url = 'http://www.163.com/'
# response = urllib.request.urlopen(url)
# print(response.read().decode())
headers={
    'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36'
}
request = urllib.request.Request(url = url,headers = headers)
response = urllib.request.urlopen(request)
print(response.read())