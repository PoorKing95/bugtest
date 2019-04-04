#cookie用来记录用户的信息。
import urllib.request
import urllib.parse

url = 'http://www.douban.com/people/193580875/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36',
    'Cookie':'viewed="26743627"; bid=d087jalTizA; gr_user_id=0ca142c1-a337-4127-8320-b0cbe0b388ab; _vwo_uuid_v2=DAE3595BD6A50560666EAED3804EF5135|7bd613da8e6c6c5221505652c904d969; ll="118159"; __utmc=30149280; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1553248707%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dtmpx-K4dmSTbXIIhBudyARTyuZe5HWbz8AVkaetQROy%26wd%3D%26eqid%3D907348fe00030a22000000035c94b1c0%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1648544304.1550585040.1553137561.1553248712.6; __utmz=30149280.1553248712.6.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ap_v=0,6.0; __yadk_uid=HlyOW3PZoMeNiyY8StdndtrxQR9gKwIu; push_noty_num=0; push_doumail_num=0; __utmv=30149280.19358; douban-profile-remind=1; dbcl2="193580875:/ajok8D74lo"; ck=hJgm; _pk_id.100001.8cb4=30f049259307ff7d.1553081022.2.1553249245.1553081025.; __utmb=30149280.17.9.1553249244840'
}
#如果只添加COOKIE不能够访问，就加入所有元素。
request = urllib.request.Request(url=url,headers = headers)
response = urllib.request.urlopen(request)

with open('class2/python/test.html', 'wb')as fp:
    fp.write(response.read())