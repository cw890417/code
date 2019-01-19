"""
多态的例子
"""
class Canvas:
	def draw_pic(self, shape):
		print("--开始绘画--")
		shape.draw(self)

class Rectangle:
	def draw(self,canvas):
		print("在%s 上绘画矩形" % canvas)
class Circle():
	"""docstring for Circle"""
	def __init__(self):
		super(Circle, self).__init__()
	
	def draw(self,canvas):
		print("在%s 上绘画圆形" % canvas)

c = Canvas()
c.draw_pic(Rectangle())
c.draw_pic(Circle())