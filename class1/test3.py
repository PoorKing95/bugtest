import urllib.request
img_url = 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2589098204,474245196&fm=26&gp=0.jpg'
response = urllib.request.urlopen(img_url)
#图片以二进制格式写入
# with open('call.jpg','wb')as fp:
#     fp.write(response.read())
#urlretrieve方法专门用来写入文件
urllib.request.urlretrieve(img_url,'duty.jpg')