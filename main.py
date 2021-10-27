# Import libraries
import json
import turtle as tur

# Getting input on what json file to use
def getFile():
	file = input("What is the name of the json file with the inputs?: ")
	f  = open(file) # Load in input file
	return f

# Get information of json file in dictionary
def getData(f):
	data = json.load(f)
	f.close() # Close file after getting information in data
	return data

# Making variables in python with information from file
def getVariables(data):
	axiom = data['axiom']
	rules = data['rules']
	alph = data['alph']
	trans = data['trans']
	return axiom, rules, alph, trans

# Apply the logic of an l-system
def lSystem(axiom, rules, iter):

	new_string = ''
	old_string = axiom # Sart with the axiom

	for _ in range(iter):
		for string in old_string:
			if string in rules:
				new_string += rules[string] # Add the rule in the new_string
			else:
				new_string += string # When the el of the string is not in rules, just add the el in the new_string
		old_string = new_string
		new_string = ''

	return old_string

# Draw the given string by using the translations
def draw(string, trans):
	screen = tur.getscreen() # Make new screen where the drawing will cmom
	t = tur.Turtle() # Initialize the turtle and give it the name "t"

	for el in string:
		if el in trans: # Check if the el can get translated
			para = trans[el][1] # Para is the parameter that will be put in the used fuction
			if "draw" == trans[el][0]:
				t.forward(para) # Draw line with length para
			elif "angle" == trans[el][0]:
				t.left(para) # Rotate to the left with "para" degrees
			elif "forward" == trans[el][0]:
				# Move forward without drawing a line
				t.penup() # Raising pen
				t.forward(para) # Moving
				t.pendown() # Dropping pen, draw again
			elif "nop" == trans[el][0]:
				pass

# Main function
def main():

	file = getFile()
	data = getData(file)
	axiom, rules, alph, trans = getVariables(data)

	# Getting input on how many iterations are needed
	iter = int(input("How many iterations of the given l-system do you want?: "))

	lstring = lSystem(axiom, rules, iter)
	draw(lstring, trans)
	tur.Screen().exitonclick() # Keep the drawing open unless you click on exit button

main()
