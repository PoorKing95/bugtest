import urllib.parse

img_url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1552992856385&di=6ccae23ad23f3cfdb63227559d2c8db4&imgtype=0&src=http%3A%2F%2Fi1.hdslb.com%2Fbfs%2Farchive%2F5a686dec191222afa5b80aae3220ae1f56cb1fd4.jpg'
#url 只能由特定的字符组成，如果出现如汉字 $ 空格等就要对其进行编码
url = 'http://www.baidu.com/index.html?wd=周杰伦'
#编码函数
ret = urllib.parse.quote(url)
#解码函数
ret1 = urllib.parse.unquote(img_url)
print(ret1)