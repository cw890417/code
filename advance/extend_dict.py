class ValueDict(dict):
	"""docstring for ValueDict"""

	def __init__(self, *args, **kwargs):
		super(ValueDict, self).__init__(*args, **kwargs)

	def getkeys(self, val):
		result = []
		for key, value in self.items():
			if value == val:
				result.append(key)
		return result


my_dict = ValueDict(a=92, 语文=92)
print(my_dict)
print(my_dict.getkeys(92))


def test(val, step):
	'''
	s生成器的定义。yield
	'''
	print("-----go------")
	cur = 0
	for i in range(val):
		cur += i * step
		yield cur


t = test(10, 1)
print(next(t))
for i in t:
	print(i, end=' ')

t1 = test(20, 1)
print(list(t1))
t2 = test(21, 1)
print(tuple(t2))

print("**************")

def square_gen(val):
	i = 0
	out_val = None
	while True:
		out_val = (yield out_val ** 2) if out_val is not None else (yield i ** 2)
		if out_val is not None:
			print("========%d" % out_val)
		i += 1

sg = square_gen(5)
print(sg.send(None))
print(next(sg))
print(sg.send(9))
print(next(sg))
