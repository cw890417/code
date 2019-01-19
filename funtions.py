#函数
#定义默认值函数
def func1(name,age = 21):
	print("name : " + name + " ,age = " + str(age))

#调用函数的几种方式
func1('chenwei')
func1('aaa',22)
func1(name = 'bbb',age = 44)

#def function(*params) 传入任意个参数
#def function(**params) 传入元组

def func01(num):
	while True:
		if num == 1:
			return 1
		return num * func01(num - 1)

val = func01(1)
print(val)
