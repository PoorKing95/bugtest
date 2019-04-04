#try与except来处理代码中可能出现的异常
#URLerror：1.没有网 2.服务器连接失败  HTTPError是URLError的一个子类(远程服务器连接成功，但是没有找到对应资源)
#同时捕获的时候，先捕获HTTPError



import urllib.request
import urllib.parse
import urllib.error

url = 'https://blog.csdn.net/mt_lf/article/details/8091591'

try:
    response = urllib.request.urlopen(url)
    print(response.read())
except urllib.error.HTTPError as e:
     print(e)
except urllib.error.URLError as e:
     print(e.code)

