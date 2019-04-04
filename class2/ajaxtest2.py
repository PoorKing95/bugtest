#ajax-post
import urllib.request
import urllib.parse

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36',
    'Connection': 'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}

city = input('请输入城市：')


data = {
    'cname':'',
    'pid':'',
    'keyword':city,
    'pageIndex':'1',
    'pageSize':'1'
}



data = urllib.parse.urlencode(data).encode()
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request,data)
print(response.read().decode())