import re
import os


#匹配以foo开始的字符串,match
m = re.match('foo','food on the table')
if m is not None:
	print(m.group())

#搜索只要出现foo就匹配成功,search
f = re.search('foo','adsfd fod foo dfdf')
if f is not None:
	print(f.group())

#传入参数的形式，参数是一个正则表达式
bt = 'asf|fds|sfs'
d = re.match(bt,'sfs')
if d is not None:
	print(d.group())

#使用‘（）’,进行分组匹配
print("-----------------------------------")
s = re.match('(a(b))','ab')
if s is not None:
	print(s.group())
	print(s.group(1))
	print(s.group(2))
	#获取元组
	print(s.groups())


#findall和finditer的区别
#findall返回的是列表，finditer返回的是对象中的迭代
print("---------------------------------")
s = 'This and that'
#re.I 忽略大小写
print(re.findall(r'(th\w+) and (th\w+)',s,re.I))
k = re.finditer(r'(th\w+) and (th\w+)',s,re.I)
for x in k:
	print(x.group())

#sub和subn都是替换,subn会返回替换的总数
print(re.sub('X', 'chenwei', 'aaa: X df X'))
print(re.subn('X', 'chenwei', 'aaa: X df X'))

print("-------------------------")
with os.popen('ls -lh /Users/chenwei','r') as f:
	for eline in f:
		print(re.split(r'\s\s+|\t', eline.strip()))