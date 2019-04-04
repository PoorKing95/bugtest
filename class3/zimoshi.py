#子模式
import re

# string = '<p><div><span>猪八戒</span></div></p>'
# pattern = re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>') 这里是子模式的使用方法

# string = '<div>困了就睡两地分居实例可</div></div></div>'
# pattern = re.compile(r'<div>.*?</div>')
string = '''fuck you son of bitch
fuck off little gril
fuck I am your lovely daddy'''
pattern = re.compile(r'^fuck', re.M)

#ret = pattern.search(string) 找一个
# 找所有的
ret = pattern.findall(string)
print(ret)
