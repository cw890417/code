class Apple():
	"""docstring for Apple"""
	def __init__(self, arg):
		super(Apple, self).__init__()
		self.arg = arg
	
	#重写描述方法，该方法属于object类，所有类都继承object
	def __repr__(self):
		return "aaaa:"+ str(self.arg)

c = Apple("asf")
print(c)