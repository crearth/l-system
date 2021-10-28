# Import libraries
import json
import turtle as tur
from datetime import datetime

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
	t.hideturtle()

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

# Check if the input file has correct input data
def checkData(axiom, rules, alph, trans, pos_translations):
	if axiom == '':
		return False

	# Check if every elemnt used is part of the given alphabet in the input file
	if not isinstance(axiom, str):
		return False
	for symbol in axiom:
		if not symbol in alph:
			return False

	if not isinstance(rules, dict):
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

	if not isinstance(alph, list):
		return False
	for symbol in alph:
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
		if not isinstance(trans[tran][1], int):
			return False
		if not trans[tran][0] in pos_translations: # Check if the translation is supported by the program
			return False

	return True

# Check if input file contains needed variables
def checkFile(data):
	if not "axiom" in data:
		return False
	if not "rules" in data:
		return False
	if not "alph" in data:
		return False
	if not "trans" in data:
		return False

	return True

# Write system history to file
def addHistory(axiom, rules, alph, trans, iterations, lstring):
	f = open("history.txt","a")
	timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	f.write(timestamp + "\t" + str(alph) + "\t" + axiom + "\t" + str(rules) + "\t" + str(trans) + "\t" + str(iterations) + "\t" + str(lstring) + "\n")	

# Main function
def main():

	file = getFile()

	# Get input on how many iterations the user wants to preform
	iter = int(input("How many iterations of the given l-system do you want to preform?: "))

	# Used_funtions is a list of the possible translations that reffer to a function
	# When you add more possible functions, add the translations of the function in the used_functions below
	used_functions = ("draw", "angle", "forward", "nop")

	data = getData(file)
	if checkFile(data) == False:
		print("The given input file is not contain the needed variabes.")
		return
	axiom, rules, alph, trans = getVariables(data)

	if checkData(axiom, rules, alph, trans, used_functions) == False:
		print("The given variables in the input file are not correct.")
		return

	lstring = lSystem(axiom, rules, iter)
	addHistory(axiom, rules, alph, trans, iter, lstring)
	print(lstring)
	draw(lstring, trans)
	tur.Screen().exitonclick() # Keep the drawing open unless you click on exit button

main()
