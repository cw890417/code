#定义类
class Dog():
	"""docstring for Dog"""
	def __init__(self, name, age):
		self.name = name
		self.age = age


	def sit(self):
		print(self.name.title() + " sit()..")


	def roll_over(self):
		print(self.name.title() + " roll_over()...")

my_dog = Dog('willie',6)
print(my_dog.name.title())
my_dog.sit()
my_dog.roll_over()