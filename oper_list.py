#操作列表
#遍历列表元素
print("for list --------")
names0 = ['aa','ss','dd','ff','gg','hh']
for name in names0:
	print(name)

#创建数值列表
#勇士range()创建
print("range() --------")
#不包含5
for value in range(1,5):
	print(value)

#使用list将range生成的数创建为列表
print("list() ---------")
values = list(range(1,5))
print(values)

#指定步长
values1 = list(range(1,10,2))
print(values1)

#列表解析
values2 = [val**2 for val in range(1,10)]
print(values2)

#处理列表的部分元素
print("切片处理----------")
values3 = ['a','b','c','d','e','f']
print(values3[0:3])
print(values3[1:4])
print(values3[:3])
print(values3[:4])
print(values3[2:])
print(values3[-3:])

#遍历切片
for val in values3[-3:]:
	print(val)

#复制列表
print("复制列表----------")
values4 = values3[:]
print(values4)


#元组，不可变的列表
print("元组-----------")
#定义元组
values5 = (22,11)
print(values5)
print(values5[0])

#遍历元组
for val in values5:
	print(val)

#if语句的应用
values6 = ['aa','bb','cc','dd','ff']
for car in values6:
	if car == 'cc':
		print(car.upper())
	else:
		print(car.title())

#使用in检查是否包含在其中
values7 = ['a','b','c','d','f']
if 'a' in values7:
	print("a in values7")
else:
	print("a not in values7")
