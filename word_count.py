#异常捕获
def count_words(filename):
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError as e:
		print("not " + filename)
	else:
		words = contents.split()
		num_word = len(words)
		print("filename:" + filename + " size : "+ str(num_word))

filename = '/Users/chenwei/code/data/pi.txt'
count_words(filename)

filenames = ['/Users/chenwei/code/data/pi.txt','/Users/chenwei/code/data/p2.txt']
for f_name in filenames:
	count_words(f_name)