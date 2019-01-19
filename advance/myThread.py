import threading
from time import sleep,ctime

loops = [4, 2]

class MyThread(threading.Thread):
	"""docstring for MyThread"""
	def __init__(self, func, args, name = ''):
		threading.Thread.__init__(self)
		self.func = func
		self.args = args
		self.name = name

	def getResult(self):
		return self.res

	def run(self):
		print("starting " + self.name + " at:" + ctime())
		self.res = self.func(*self.args)
		print("finished " + self.name + " at:" + ctime())