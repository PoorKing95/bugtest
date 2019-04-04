import urllib.request
import urllib.parse
import os


url='http://tieba.baidu.com/f?ie=utf-8'
#输入吧名，起始页码和结束页码，在当前文件夹中写入吧名_page.html
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36',
    'Connection': 'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}

sp = int(input('开始页码：'))
ep = int(input('结束页码:'))

name = input('请输入吧名：')
if not os.path.exists('class2/'+name):
    os.makedirs('class2/'+name)
for page in range(sp,ep+1):
    real = (page-1)*50
    data={
    'kw':name,
    'pn':real
    }
    data = urllib.parse.urlencode(data)
    tmp = url + '&' + data
    request = urllib.request.Request(url=tmp,headers=headers)

    print('开始下载第%s页……'%page)
    response = urllib.request.urlopen(request)
    filename = name+'_'+str(page)+'.html'
    filepath = 'class2/'+name+'/'+filename
    with open(filepath, 'wb')as fp:
        fp.write(response.read())
    print('载第%s页下载结束……'%page)
