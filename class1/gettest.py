import urllib.request
import urllib.parse

word = input('输入搜索')
url = 'http://www.baidu.com/s?'

data={
    'ie':'utf-8',
    'wd':word
}
#这部分很重要
query_string = urllib.parse.urlencode(data)
url += query_string
#发送请求
response = urllib.request.urlopen(url)
filename = word + '.html'
with open(filename,'wb') as fp:
    fp.write(response.read())