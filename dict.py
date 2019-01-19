from collections import OrderedDict
#字典
#创建字典
values1 = {'a':'1','b':'2'}
print(values1['a'])
print(values1['b'])

#添加键值对
values1['c'] = '3'
print(values1)

#删除键值对
del values1['c']
print(values1)

#遍历字典,items()
print("通过items遍历---------")
for k,v in values1.items():
	print(k+" : " + v)

#遍历keys
print("用过keys遍历----------")
for k in values1.keys():
	print("k = " + k)

#遍历values
print("用过values遍历----------")
for v in values1.values():
	print("v = " + v)

#字典存储元组
print("遍历存储元组的字典----------")
values2 = {'a':['1','2'],'b':['3','4']}
for key,vals in values2.items():
	print("k : " + key)
	for v in vals:
		print("val = " + v)

#while循环
print("while 循环------------")
number = 1
while number <= 5:
	print(number)
	number += 1

#有序的字典
dict01 = OrderedDict()
dict01['aa'] = '11'
dict01['bb'] = '22'
dict01['cc'] = '33'
for k,v in dict01.items():
	print(k.title() + " " + v)

