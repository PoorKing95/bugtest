import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/v2transapi'
word = input('请输入：')
formdata={
    'from':'en',
    'to':'zh',
    'query':word,
    'transtype':'enter',
    'simple_means_flag':'3',
    'sign':'431039.159886',
    'token':'0859cf14e34a5977bf9320c6d6fb879b'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36',
    'Host': 'fanyi.baidu.com',
    'Connection': 'keep-alive',
    'Content-Length': '121',
    'Accept': '*/*',
    'Origin': 'https://fanyi.baidu.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://fanyi.baidu.com/',
    #'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'BDUSS=FhdXJJZTFKQjNUS35QfndHVE1nYlZ4NUhTMFhHMTUyS0VyYnJJOG9mT2N6SGhiQUFBQUFBJCQAAAAAAAAAAAEAAABoce09s8nIq7TztdsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJw~UVucP1FbUV; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_cc903faaed69cca18f7cf0997b2e62c9=1539652310; Hm_lvt_4e5bdf78b2b9fcb88736fc67709f2806=1542011776,1542013382,1543652661; BAIDUID=098AD152E61AB4A379FD39732B2FF090:FG=1; PSTM=1550465282; BIDUPSID=B3716F9C73FF425EE8048CE05961AE2D; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1434_21121_28723_28557_28584_28603_28625_22158; delPer=0; PSINO=1; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1553069104; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1553075525; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0'

}

request = urllib.request.Request(url=post_url,headers=headers)
formdata = urllib.parse.urlencode(formdata).encode()
response = urllib.request.urlopen(request, formdata)
teststr = response.read()
with open('test.txt','wb') as fp:
    fp.write(teststr)