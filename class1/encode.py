import urllib.parse
url = 'http://www.baidu.com/index.html'
#假设参数
name = '张三'
age = 18
sex = 'female'

data={
    'name':name,
    'sex':sex,
    'age':age
}
# lt = []
# for i, v in data.items():
#     lt.append(i + '=' +str(v))
# query_string = '&'.join(lt)

#urlencode直接把字典编码成了合法字符，并且转为超链接形式
query_string = urllib.parse.urlencode(data)

url = url+'?'+query_string
print(query_string)
print(url)