class Queue:
	def __init__ (self, list):
		self.list = list;

	def getPosition (self, index):
		return self.list[index]

class User:
	def __init__ (self, name, hall, room):
		self.name = name
		self.hall = hall
		self.room = room

	def output (self):
		return "My name is " + self.name + " and I live in " + self.room + " " + self.hall

local_name = raw_input ("What is your name? \n")
local_hall = raw_input ("What hall do you live in? \n")
local_room = raw_input ("What is your room number? \n")

new_user = User(local_name, local_hall, local_room)

shower = Queue([])
washer = Queue([])
dryer = Queue([])
user_list = [new_user]
 
print(new_user.output())