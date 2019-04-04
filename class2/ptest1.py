import urllib.request
import urllib.parse

url = 'http://fanyi.baidu.com/sug'
url_1 = 'http://fanyi.baidu.com/langdetect'
url_2 = 'http://fanyi.baidu.com/v2transapi'
word = input('输入单词:')
form1_data={
    'kw':word
}
form2_data={
    'query':word
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)
#处理表单
form_data1 = urllib.parse.urlencode(form1_data).encode()
form_data2 = urllib.parse.urlencode(form2_data).encode()
#发送请求
response1 = urllib.request.urlopen(request, data=form_data1)

print(response1.read().decode('utf8'))