from atexit import register
from re import compile
from threading import Thread
from urllib.request import urlopen as uopen
from time import ctime
import ssl

regex = compile('#([\d,]+) in Books ')
amzn = 'http://amazon.com/dp/'
isbns = {
	'0132269937':'core python programming',
	'0132356139':'python web development',
	'0137143419':'python fundamentals'
}

def getRanking(isbn):
	page = uopen('%s%s' % (amzn,isbn))
	data = page.read()
	page.close()
	return regex.findall(data)[0]

def _showRanking(isbn):
	print('- %r ranked %s' % (isbns[isbn],getRanking(isbn)))

def main():
	print("at "+ctime()+" on amazon")
	for isb in isbns:
		_showRanking(isb)

@register
def _atexit():
	print("all done at "+ ctime())

if __name__ == '__main__':
	main()