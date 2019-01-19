class Cell():
	"""docstring for Cell"""
	def __init__(self):
		super(Cell, self).__init__()
	
	
	@property
	def state(self):
		return self._state
    
	@state.setter
	def state(self,value):
		if 'alive' in value.lower():
			self._state = 'alive'
		else:
			self._state = 'dead'

	@property
	def is_dead(self):
		return not self._state.lower() == 'alive'
	
c = Cell()
c.state = 'alive'

import os
print(os.__file__)
