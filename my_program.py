if 3 > 2:
	print('It works!')


def hi(name):	
	print('Hi ' + name + '!')

hi('Belle')


class Car:
	def __str__(self):
		return 'Car: ' + self.name

	def __init__(self, name):
		self.name  = name

	def run(self):
		print(self.name + ' Run!')

benz = Car('ted')
benz.run()
print(benz)


boys = ['ted 1', 'ted 2', 'ted 3']

for name in boys:
	hi(name)


