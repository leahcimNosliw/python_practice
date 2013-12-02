import random

class Die(object):
	'''
	This class represents a die that can be rolled to generate a random
	number.
	'''
	
	def __init__(self, max_roll):
		'''
		Ctor - Initialises the die to be rolled.
		'''
		self._max_roll = max_roll + 1
	
	def roll(self):
		'''
		Rolls the die. Returns the result.
		'''
		roll = random.randrange(0, self._max_roll)
		while roll == 0:
			roll = random.randrange(0, self._max_roll)
		return roll

class D6(Die):
	'''
	This class represents a D6 that can be rolled to generate a random
	number between 1 and 6.
	'''
	
	def __init__(self):
		'''
		Ctor - Initialises the D6.
		'''
		Die.__init__(self, 6)

die = D6()
result = die.roll()
print(result)
