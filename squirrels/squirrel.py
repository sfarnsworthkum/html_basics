class Squirrel():
	count = 1

	def __init__(self,name):
		self.name = name
		self.id = Squirrel.count
		Squirrel.count += 1