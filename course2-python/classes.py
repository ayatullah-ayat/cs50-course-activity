class Flight():
	"""docstring for Flight"""
	def __init__(self, capacity):
		self.capacity = capacity
		self.passengers = []
	
	def add_passengers(self, name):
		if self.open_seats() == 0:
			return False
		self.passengers.append(name)
		return True

	def open_seats(self):
		return self.capacity - len(self.passengers)

flight = Flight(3)
people = ['Harry', 'Potter', 'Williamson', 'Holder', 'Maxwell']

for person in people:
	sucess = flight.add_passengers(person)
	if sucess:
		print(f'Added {person} to flight sucessfully')
	else:
		print(f'Not added {person} to flight sucessfully')