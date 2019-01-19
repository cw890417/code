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
		#print("starting " + self.name + " at:" + ctime())
		self.res = self.func(*self.args)
		#print("finished " + self.name + " at:" + ctime())

def loop(nloop,nsec):
	print("start loop "+ str(nloop) + " at : " + ctime())
	sleep(nsec)
	print("loop " + str(nloop) + " done at:" + ctime())

def main():
	print("starting at:" +ctime())
	threads = []
	nloops = range(len(loops))
	for i in nloops:
		t = MyThread(loop,(i, loops[i]),loop.__name__)
		threads.append(t)

	for i in nloops:
		threads[i].start()

	for i in nloops:
		threads[i].join()

	print("all done at:" + ctime())

if __name__ == '__main__':
	main()