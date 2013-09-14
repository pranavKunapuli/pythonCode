import math 

vector1x = int(raw_input("Vector 1 i coefficient: "))
vector1y = int(raw_input("Vector 1 j coefficient: "))
vector1z = int(raw_input("Vector 1 k coefficient: "))

vector1 = [vector1x, vector1y, vector1z]

vector2x = int(raw_input("Vector 2 i coefficient: "))
vector2y = int(raw_input("Vector 2 j coefficient: "))
vector2z = int(raw_input("Vector 2 k coefficient: "))

vector2 = [vector2x, vector2y, vector2z]

def dot_product (vector1 , vector2):
	x_product = vector1[0] * vector2[0]
	y_product = vector1[1] * vector2[1]
	z_product = vector1[2] * vector2[2]

	return x_product + y_product + z_product

def cross_product (vector1, vector2):
	i_coeffient = (vector1[1] * vector2[2]) - (vector1[2] * vector2[1])
	j_coeffient = (vector1[0] * vector2[2]) - (vector1[2] * vector2[0])
	k_coeffient = (vector1[0] * vector2[1]) - (vector1[1] * vector2[0])

	cross = [i_coeffient, j_coeffient, k_coeffient]

	return cross

request = ""

while(request.lower != "dot" and request.lower() != "cross"):
	print "Enter only the words dot or cross"
	request = raw_input("Would you like to calculate the dot product or the cross product: ")
	
	if request.lower() == "dot":
		print str(dot_product (vector1, vector2))
	elif request.lower() == "cross":
		cross_result = cross_product (vector1, vector2)

		for values in range(len(cross_result)):
			if values == 0:
				print "Vector = " + str(cross_result[values]) + "i",
			elif values == 1:
				print " + " + str(cross_result[values]) + "j",
			else:
				print " + " + str(cross_result[values]) + "k"
	else:
		print "That's not a valid input you idiot"