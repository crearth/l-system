# Import libraries
import json
import turtle as tur
from datetime import datetime
import sys, getopt

# Getting input on what json file to use
def getFile():
	"""
	Input: None
	----------
	Output: Return file that is given by the user of the program
	"""
	file = input("What is the name of the json file with the inputs?: ")
	f  = open(file) # Load in input file
	return f

# Get information of json file in dictionary
def getData(f):
	"""
	Input: File
	----------
	Output: Return a dictionary of the content of the given file 
	"""
	data = json.load(f)
	f.close() # Close file after getting information in data
	return data

# Making variables in python with information from file
def getVariables(data):
	"""
	Input: Dictionary with neede variables for an l-system
	----------
	Output: Return the needed variables for an l-system
	"""
	axiom = data['axiom']
	rules = data['rules']
	variables = data['variables']
	constants = data['constants']
	trans = data['trans']
	return axiom, rules, variables, constants, trans

# Apply the logic of an l-system
def lSystem(axiom, rules, iter):
	"""
	Input: Axiom = string, rules = dictionary, iterations (iter) = int
	----------
	Output: The resulting string after preforming the l-system with the inputs
	"""
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

# Change the color of the drawing
def setColor(color, t):
	"""
	Input: Color = string (with name of a color), t = a python turtle
	----------
	Output: Python turtle with the given color
	"""
	t.pencolor(color)
	return t

# Draw the given string by using the translations
def draw(string, trans, imageName):
	"""
	Input: String (the end result of an l-system), translations (trans) = dictionary (the trans of the used l-system
	----------
	Output: No return, will draw the given string by the given translations
	"""
	screen = tur.getscreen() # Make new screen where the drawing will come
	t = tur.Turtle() # Initialize the turtle and give it the name "t"
	t.hideturtle()
	t.setheading(90) # Set starting position of turtle heading up
	t.speed(0)

	stack = [] # Stack will be used to push and pop between positions

	for symbol in string:
		if symbol in trans: # Check if the el can get translated
			para = trans[symbol][1] # Para is the parameter that will be put in the used fuction
			if "draw" == trans[symbol][0]:
				t.forward(para) # Draw line with length para
			elif "angle" == trans[symbol][0]:
				t.left(para) # Rotate to the left with "para" degrees
			elif "forward" == trans[symbol][0]:
				# Move forward without drawing a line
				t.penup() # Raising pen
				t.forward(para) # Moving
				t.pendown() # Dropping pen, draw again
			elif "nop" == trans[symbol][0]:
				pass
			elif "push" == trans[symbol][0]:
				stack.append((t.pos(), t.heading())) # Add the current position and heading to stack
			elif "pop" == trans[symbol][0]:
				t.penup()
				t.setpos(stack[len(stack)-1][0]) # Set position and heading to last item in stack
				t.setheading(stack[len(stack)-1][1])
				t.pendown()
				stack.pop(len(stack)-1) # Remove last item from stack
			elif "color" == trans[symbol][0]:
				setColor(trans[symbol][1], t)

	# If the imageName is not None, make an eps file with the name imageName
	if imageName != None:
		screen.getcanvas().postscript(file=imageName)

# Check if the input file has correct input data
def checkData(axiom, rules, alph, trans, pos_translations):
	"""
	Input: All the variables of an l-system and the translations of the string that our program supports
		axiom = string, rules = dictionary, alph = list, trans = list, pos_translations = list (supported translations)
	----------
	Output: Return False if the data is not the correct data to preform an l-system
	"""
	if axiom == '': # We need an axiom to start the program
		return False

	if not isinstance(axiom, str): # Check if axiom is a string
		return False
	for symbol in axiom: # Check if every symbol in axiom is in the alphabet
		if not symbol in alph:
			return False

	if not isinstance(rules, dict): # Check if rules is a dictionary
		return False
	for rule in rules:
		if not rule in alph: # Rules is a dictionary, rule is a key
			return False
		for symbol in rules[rule]: # Symbol is every symbol in the value of the given key
			if symbol not in alph:
				return False
		if not isinstance(rule, str):
			return False
		if not isinstance(rules[rule], str):
			return False

	if not isinstance(alph, list): # Check if the alphabet is a list
		return False
	for symbol in alph: # Check if every symbol in the alphabet is a string
		if not isinstance(symbol, str):
			return False

	if not isinstance(trans, dict):
		return False
	for tran in trans: # Trans is a dictionary, tran is a key in trans
		if not tran in alph:
			return False
		if not isinstance(trans[tran] , list): # Trans[tran] is the value of the key 
			return False
		if not isinstance(trans[tran][0], str): # Trans[tran][1] is the second item in the value of the key, the value is a list
			return False
		if trans[tran][0] == "color": # When the function is color, we need a string not a value
			if not isinstance(trans[tran][1], str):
				return False
		else:
			if not (isinstance(trans[tran][1], int) or isinstance(trans[tran][1], float)):
				return False
		if not trans[tran][0] in pos_translations: # Check if the translation is supported by the program
			return False

# Check if input file contains needed variables
def checkFile(data):
	"""
	Input: List (data of the input file)
	----------
	Output: Return False if the needed variables are not in the input file
	"""
	if not "axiom" in data:
		return False
	if not "rules" in data:
		return False
	if not "variables" in data:
		return False
	if not "constants" in data:
		return False
	if not "trans" in data:
		return False

	return True

# Write system history to file
def addHistory(axiom, rules, alph, trans, iterations, lstring, variables, constants):
	"""
	Input: All variables that need to be stored in the history file
	----------
	Output: Add a line with the variables to history.txt
	"""
	f = open("history.txt","a")
	timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	f.write(timestamp + "\t" + str(variables) + "\t" + str(constants) + "\t" + axiom + "\t" + str(rules) + "\t" + str(trans) + "\t" + str(iterations) + "\t" + str(lstring) + "\n")	

# Make alphabet variable
def makeAlph(variables, constants):
	"""
	Input: Variables = list, constants = list
	----------
	Output: List (The alphabet of the l-system = variables + constants)
	"""
	alph = variables + constants
	return alph

def getArguments(argv):
	outputfile = '' # Initialize the variable outputfile
	try:
		opts, args = getopt.getopt(argv,"-e",["export="]) # Get the options and arguments
	except getopt.GetoptError:
		print("main.py --export <filename>") # If there is an error, print how to use the option
	# Get the options and arguments and set it to the variable outputfile
	# If there is no option, set outputfile to False
	for opt, arg in opts:
		if opt in ("-e", "--export"):
			outputfile = arg
		else:
			 outputfile = False
	return outputfile

# Main function
def main():

	file = getFile()

	# Get input on how many iterations the user wants to preform
	iter = int(input("How many iterations of the given l-system do you want to preform?: "))

	# Used_funtions is a list of the possible translations that reffer to a function
	# When you add more possible functions, add the translations of the function in the used_functions below
	used_functions = ("draw", "angle", "forward", "nop", "push", "pop", "color")

	data = getData(file)
	if checkFile(data) == False:
		print("The given input file is not contain the needed variabes.")
		return

	axiom, rules, variables, constants, trans = getVariables(data)
	alph = makeAlph(variables, constants)

	if checkData(axiom, rules, alph, trans, used_functions) == False:
		print("The given variables in the input file are not correct.")
		return

	lstring = lSystem(axiom, rules, iter)
	addHistory(axiom, rules, alph, trans, iter, lstring, variables, constants)

	print(lstring)

	# Give the draw function the name of the file, if there is one
	argument = getArguments(sys.argv[1:])
	if argument != False:
		draw(lstring, trans, argument)
	else:
		draw(lstring, trans, None)

	tur.Screen().exitonclick() # Keep the drawing open unless you click on exit button

main()
