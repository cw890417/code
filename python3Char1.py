#变量的定义，列表的介绍
print("hello world!")
message = "hello python world! 'sdf' "
print(message)

#对字符串的操作
name = "adas asdff"
print(name.title())
print(name.upper())
print(name.lower())

#数值和字符串的转换
age = 23
print("happy " + str(age) + "rd aa!")

####################################
#列表
bicycles = ['asf','qwr','zxc','fff']
print(bicycles)
#访问列表
print(bicycles[0].title())

#访问列表最后一个元素,下标-1
#倒数第二个元素-2，依次类推
print(bicycles[-1])

#修改列表元素
names = ['chenwei','jok','djha']
print()
names[0] = 'chenwei1'
print(names)

#添加列表内容
names.append('qwerr') #末尾添加元素
print(names)

#制定位置添加元素
names.insert(2,'chennn')
print(names)

#删除列表元素
#del 方法删除
print("del ----------")
del names[2]
print(names)

#pop删除元素,默认最后一个元素
#当使用pop后，该元素在列表中就不存在了
print("pop() ------------")
names1 = ['aa','bb','cc','dd']
print(names1)
popped_names1 = names1.pop()
print(names1)
print(popped_names1)

#删除指定位置的元素，通过pop()
names2 = ['aa','bb','cc','dd']
popped_names2 = names2.pop(2)
print(names2)
print(popped_names2)

#根据值删除元素remove(),该方法只会删除第一个值
print("remove() ----------")
names3 = ['aa','bb','cc','dd','dd']
print(names3)

names3.remove('cc')
#通过变量的形式指定之
remove_val = 'dd'
names3.remove(remove_val)
print(names3)

#组织列表
#使用sort进行排序,修改是永久的
print("sort() -------")
names4 = ['ff','dd','aa','cc']
print(names4) 
names4.sort()
print(names4)
names4.sort(reverse = True)
print(names4)

#使用sorted对列表进行临时排序
print("sorted() ----------")
names5 = ['ee','aa','cc','bb']
print(names5)
print(sorted(names5))
print(names5)

#通过reverse()对列表进行反转,永久的修改列表
print("reverse() ---------")
names6 = ['fdf','ss','dd','aa','fd']
names6.reverse()
print(names6)

#统计列表的长度len
print("len() ---------")
names7 = ['a','f','d','s','r','e']
print(len(names7))