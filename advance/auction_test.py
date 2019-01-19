class AuctionException(Exception):
	pass


class AuctionTest():
	"""docstring for AuctionTest"""
	def __init__(self, init_price):
		super(AuctionTest, self).__init__()
		self.init_price = init_price
		
	def bid(self, bid_price):
		d = 0.0
		try:
			d = float(bid_price)
		except Exception as e:
			print("转换出异常",e)
			raise AuctionException("必须是数值")
		if self.init_price > d:
			raise AuctionException("数值太小")
		initPrice = d

def main():
	at = AuctionTest(20.4)
	try:
		at.bid(4)
	except AuctionException as e:
		print("函数异常:",e)

main()

		