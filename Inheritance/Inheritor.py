class Parent():
	def __init__(self, last_name, eye_color):
		print('parent constructor called.')
		self.last_name = last_name
		self.eye_color = eye_color

	def show_stats(self):
		print('Last Name: ' + self.last_name)
		print('Eye color: ' + self.eye_color)

class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		print('child constructor called.')
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

	def show_stats(self):
		print('Last Name: ' + self.last_name)
		print('Eye color: ' + self.eye_color)
		print('Number of toyes: ' + self.number_of_toys)


john_doe = Parent("Doe", "green")
junior_doe = Child('Doe', 'green', '4')

if junior_doe.show_stats() == None:
	print(' ')
else:
	print(junior_doe.show_stats())
