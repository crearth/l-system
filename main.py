# Import json library
import json

# Getting input on what json file to use
def getFile():
	file = input("What is the name of the json file with the inputs?: ")
	# Loading in input file
	f  = open(file)
	return f

# Get information of json file in dictionary
def getData(f):
	data = json.load(f)
	# Close file after getting information in data
	f.close()
	return data

# Making variables in python with information from file
def getVariables(data):
	axiom = data['axiom']
	rules = data['rules']
	alph = data['alph']
	trans = data['trans']
	return axiom, rules, alph, trans

# L-system function
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

# Define main function
def main():

	file = getFile()
	data = getData(file)
	axiom, rules, alph, trans = getVariables(data)

	# Getting input on how many iterations are needed
	iter = int(input("How many iterations of the given l-system do you want?: "))

	lstring = lSystem(axiom, rules, iter)
	print(lstring)

main()
