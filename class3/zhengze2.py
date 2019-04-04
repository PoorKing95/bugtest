import re


def fn(a):
    ret = int(a.group())
    return str(ret + 10)
string = '我想长到180的身高175'
pattern = re.compile(r'\d+')
# ret = pattern.findall(string)
# high = str(int(ret[0])+5)
# ret = pattern.sub(high,string)
# print(ret)
# 另一种 写法
ret = pattern.sub(fn, string)
print(ret)