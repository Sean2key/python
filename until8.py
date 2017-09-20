class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name)

	def roll(self):
		print(self.age)

mydog = Dog('dowu', 3)
mydog.sit()
mydog.roll()