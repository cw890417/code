x = map(lambda x: x * x, range(1,8))
print([e for e in x])

class Dog():
	"""docstring for Dog"""
	def __init__(self, arg):
		super(Dog, self).__init__()
		self.arg = arg

	def run(self):
		print("running ..")

#通过类调用对象，不会自动绑定self
Dog.run("aa")

#通过实例调用，会自动绑定self
p = Dog("aa")
p.run()

print("---------------")

"""
1.将funB做为参数，传递给funA：funA(funB)
2.funB替换成第一步的结果，变为字符串（有funA的返回值决定）
"""
def funA(fn):
	print("A")
	fn()
	return 'fkit'

@funA
def funB():
	print("B")

print(funB)

print("----------")

def auto(fn):
	def auto_fn(*args):
		print("权限检查。。。。")
		fn(*args)
	return auto_fn

@auto
def test(a,b,c):
	print("a: %s, b:%s" % (a,b))

print(test("asas","asa","dsd"))