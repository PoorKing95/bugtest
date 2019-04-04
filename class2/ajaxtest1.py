#ajax-get
import urllib.request
import urllib.parse 
url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&'

number = 20
page = int(input('第几页:'))
data ={
    'start':(page-1)*20
}
query_string = urllib.parse.urlencode(data)
url = url+query_string

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf8'))