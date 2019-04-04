#正则1
import re

string = '''<div>
    烟笼寒水月笼沙
    夜泊秦淮近酒家
    商女不知亡国恨
    隔江犹唱后庭花
</div>'''

pattern = re.compile(r'[\n](.*)</div>', re.S)
ret = pattern.findall(string)
print(ret)

inner = 'i hate you, you are son of bitch'
pattern = re.compile(r'you')
ret = pattern.sub('huan',inner)
print(ret)