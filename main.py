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

	for _ in range(iter): # Preform the rules as much as the iteration input says
		for string in old_string: # Go over every symbol in the string
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

# Init turtle, screen
def drawInit(): # Subfunction from draw
	'''
	Input: None
	----------
	Output: Return screen and turtle
	'''
	screen = tur.Screen() # Set up screen

	t = tur.Turtle() # Initialize the turtle and give it the name "t"
	t.hideturtle() # Hide the turtle on the screen
	t.setheading(90) # Set starting position of turtle heading up
	screen.tracer(0,0) # Doesn't show the turtle until screen.update()
	# This makes the drawing faster
	return screen, t

# Draw the string
def drawDraw(string, trans, screen, t):
	'''
	Input: String , trans is the translations (dictionary), screen is a turtle screen
	t is the turtle itself
	----------
	Ouput: Return screen and turtle
	'''

	stack = [] # Stack will be used to push and pop between positions

	svgCoordinates = [] # Initialize the list

	width, height = 0,0 # Start width and height width 0,0

	for symbol in string: # Go over every symbol in the generated lstring
		if symbol in trans: # Check if the el can get translated
			para = trans[symbol][1] # Para is the parameter that will be put in the used function
			function = trans[symbol][0] # Function is the string of the function in the json file
			if "draw" == function:
				x1, y1 = t.pos() # The starting point of the line
				t.forward(para) # Draw line with length para
				x2, y2 = t.pos() # The end point of the line
				svgCoordinates.append((x1, y1, x2, y2)) # Add the beginning and end coordinates to the list of coordinates
			elif "angle" == function:
				t.left(para) # Rotate to the left with "para" degrees
			elif "forward" == function:
				# Move forward without drawing a line
				t.penup() # Raising pen
				t.forward(para) # Moving
				t.pendown() # Dropping pen, draw again
			elif "nop" == function:
				pass # Do nothing
			elif "push" == function:
				stack.append((t.pos(), t.heading())) # Add the current position and heading to stack
			elif "pop" == function:
				t.penup() # Make sure no lines are drawn
				t.setpos(stack[-1][0]) # Set position and heading to last item in stack
				t.setheading(stack[-1][1]) # Set heading to last item in stack
				t.pendown() # Make sure turtle draws again
				stack.pop(-1) # Remove last item from stack
			elif "color" == function:
				setColor(para, t)

			# Set the width and height to the max values of x and y
			width = abs(max(width, abs(t.pos()[0])))
			height = abs(max(height, abs(t.pos()[1])))

	# Multiply width 2.2 so we have a border around the drawing
	width *= 2.2
	height *= 2.2

	# Write the svg file width the coordinates of all the lines in the drawing
	makeText(svgCoordinates, width, height)

	return screen, t, width, height


# Make the text for the svg file
def makeText(coordinates, width, height):
	'''
	Input: a list of coordinates like [(x1,y1,x2,y2), ...]
	----------
	Output: no return, will write the svg file that we later use in webPage.py
	'''

	svg = open("./static/.lstring.svg", "w") # Open file

	# xAdd and yAdd are needed because svg has (0,0) in the top left corner and turtle in the middle of the screen
	# We will add xAdd to every x and yAdd to every y, this will make the drawing start in the middle of the screen
	xAdd = width/2
	yAdd= height/2

	svgText = [] # Initialize the list
	for coord in coordinates:
		# Get coordinates from list
		x1 = coord[0]
		x2 = coord[2]
		y1 = coord[1]
		y2 = coord[3]
		# Add text with the coordinates
		# The text that we add is svg code for a line and it uses the beginning and end coordinates
		svgText.append('<line x1="' + str(x1+xAdd) + '" y1="' + str(-y1+yAdd) + '" x2="' + str(x2+xAdd) + '" y2="' + str(-y2+yAdd) + '" style="stroke:rgb(0,0,0);stroke-width:0.5" />\n')

	# Insert the start svg tag
	svgText.insert(0, '<svg width="' + str(width/2) + '" height="' + str(height/2) + '">\n')
	# Add the end svg tag
	svgText.append('</svg>')
	svg.writelines(svgText) # Write the lines in the file

	svg.close() # Close file

# Save the drawing
def drawSave(imageName, screen, width, height): # Subfunction of draw
	'''
	Input: ImageName if there is one, screen and turtle
	----------
	Output: Save the drawing, no return
	'''
	screen.screensize(width, height)
	screen.update() # Update screen after drawing
	# If the imageName is not None, make an eps file with the name imageName
	if imageName != None:
		screen.getcanvas().postscript(file=imageName, width=width, height=height)

# Draw the given string by using the translations
def draw(string, trans, imageName):
	"""
	Input: String (the end result of an l-system), translations (trans) = dictionary (the trans of the used l-system
	----------
	Output: No return, will draw the given string by the given translations
	and save the drawing in static under the name lastDrawing.(eps/jpg)
	"""

	screen, t = drawInit() # Set up screen and turtle (t)
	screen, t, width, height = drawDraw(string, trans, screen, t) # Make the drawing
	drawSave(imageName, screen, width, height) # Save the drawing and export function

# Check if axiom is correct data type
def checkAxiom(axiom, alph):
	'''
	Input: axiom and alph
	----------
	Output: return True if axiom is string with all symbols in alph
	else return False
	'''
	if axiom == '': # We need an axiom to start the program
		return False

	if not isinstance(axiom, str): # Check if axiom is a string
		return False
	for symbol in axiom: # Check if every symbol in axiom is in the alphabet
		if not symbol in alph:
			return False
	return True

# Check if the rules have the correct data type
def checkRules(rules, alph):
	'''
	Input: rules and alph
	----------
	Output: return True if rules is dict with [string : list] and all symbols in alph
	else return False
	'''
	if not isinstance(rules, dict): # Check if rules is a dictionary
		return False
	for rule in rules:
		if not rule in alph: # Rules is a dictionary, rule is a key
			return False
		for symbol in rules[rule]: # Symbol is every symbol in the value of the given key
			if symbol not in alph:
				return False
		if not isinstance(rule, str): # Check if rule is a string
			return False
		if not isinstance(rules[rule], str): # Check if the value of every rule is a string
			return False
	return True

# Check if the alphabet is the correct data type
def checkAlph(alph):
	'''
	Input: alph
	----------
	Output: return True if alph is a list from strings
	else return False
	'''
	if not isinstance(alph, list): # Check if the alphabet is a list
		return False
	for symbol in alph: # Check if every symbol in the alphabet is a string
		if not isinstance(symbol, str):
			return False
	return True

# Check if the translations has the correct data type
def checkTrans(trans, alph, pos_translations):
	'''
	Input: trans, alph, pos_translations
	----------
	Output: return True if trans is dict with [string : list] and all those strings are in pos_translations
	else return False
	'''
	if not isinstance(trans, dict):
		return False
	for tran in trans: # Trans is a dictionary, tran is a key in trans
		if not tran in alph:
			return False
		if not isinstance(trans[tran] , list): # Trans[tran] is the value of the key
			return False
		if not isinstance(trans[tran][0], str): # Trans[tran][1] is the second item in the value
			return False
		if trans[tran][0] == "color": # When the function is color, we need a string not a value
			if not isinstance(trans[tran][1], str):
				return False

		elif not (isinstance(trans[tran][1], int) or isinstance(trans[tran][1], float)): # The parameter must be an int
			return False
		elif not trans[tran][0] in pos_translations: # Check if the tran>
			return False

	return True

# Check if the input file has correct input data
def checkData(axiom, rules, alph, trans, pos_translations):
	"""
	Input: All the variables of an l-system and the translations of the string that our program supports
		axiom = string, rules = dictionary, alph = list, trans = list, pos_translations = list (supported translations)
	----------
	Output: Return False if the data is not the correct data to preform an l-system
	"""
	if checkAxiom(axiom, alph) and checkRules(rules, alph) and checkAlph(alph) and checkTrans(trans, alph, pos_translations):
		return True
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
def addHistory(axiom, rules, trans, iterations, lstring, variables, constants):
	"""
	Input: axiom (string), rules (dictionary), trans (dictionary), iterations (integer), lstring (string), variables (list), constants (list)
	----------
	Output: the line with history information that has to be written in history.txt
	"""
	f = open("history.txt","a") # Open the history.txt file (or make one if it doesn't exist) in the append mode 
	timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # Get current timestamp in day/month/year hour:minute:second notation
	info = timestamp + "\t" + str(variables) + "\t" + str(constants) + "\t" + axiom + "\t" + str(rules) + "\t" + str(trans) + "\t" + str(iterations) + "\t" + str(lstring) + "\n" # Concatenate all the input to one line with tabs between two variables, also convert the variable to a string if needed to be able to concatenate
	f.write(info) # Write the history data to the file
	return info # Return the history information (used for pytest)

# Make alphabet variable
def makeAlph(variables, constants):
	"""
	Input: Variables = list, constants = list
	----------
	Output: List (The alphabet of the l-system = variables + constants)
	"""
	alph = variables + constants # The alphabet is the combination of variables and constants
	return alph

def getArguments():
	"""
	Input: None
	---------
	Output: return the name of the outputfile if there is an argument "export", otherwise return None
	"""
	try:
		opts, args = getopt.getopt(sys.argv[1:], '',["export="]) # Get the options and arguments, we need one long argument 'export'
	except getopt.GetoptError:
		print("main.py --export <filename>") # If there is an error, print how to use the option
	# Get the options and arguments and return the argument of the export option
	# If there is no option, return  None
	for opt, arg in opts:
		if opt == "--export":
			return arg 
	return None 

# Main function
def main():

	file = getFile()

	# Get input on how many iterations the user wants to preform
	iter = int(input("How many iterations of the given l-system do you want to preform?: "))

	# Used_funtions is a list of the possible translations that reffer to a function
	# When you add more possible functions, add the translations of the function in the used_functions below
	used_functions = ("draw", "angle", "forward", "nop", "push", "pop", "color")

	# Get a dictionary with the variables
	data = getData(file)
	if checkFile(data) == False: # Check if the file has the needed variables
		print("The given input file is not contain the needed variabes.")
		return

	# Get the variables in the python file
	axiom, rules, variables, constants, trans = getVariables(data)
	# Make the alphabet
	alph = makeAlph(variables, constants)

	# Check if the variables have the right variable type
	if checkData(axiom, rules, alph, trans, used_functions) == False:
		print("The given variables in the input file are not correct.")
		return

	# Apply the logic of an l-system
	lstring = lSystem(axiom, rules, iter)
	# Add the l-system to the history file
	addHistory(axiom, rules, trans, iter, lstring, variables, constants)

	# Print l-string to terminal
	print(lstring)

	# Give the draw function the name of the file to export, if there is one
	imageName = getArguments()
	draw(lstring, trans, imageName)

	tur.Screen().exitonclick() # Keep the drawing open unless you click on exit button

if __name__ == "__main__":
   # Function only to run when not called via 'import' 
   main()
