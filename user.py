class User:
	def __init__(self, name, ID):
		self.name = name
		self.id = ID

	def out(self):
		print self.name
		print self.id

pranav = User("Pranav", 12053234)
pranav.out();

class Queue:
	def __init__(self):
		self.list = []

	def enq(self,user):
		self.list.append(user)

	def deq(self):
		first = self.list[0]
		self.list.remove(first)
		return first

	def retrieve(self, index):
		return self.list[index]

q = Queue()
q.enq(pranav)
new = q.retrieve(0)
new.out()
q.deq().out()