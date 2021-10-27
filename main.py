# Import json library
import json

# Getting input on what json file to use
file = input("What is the name of the json file with the inputs?: ")

# Loading in input file
f = open(file)

# Get information of json file in dictionary
data = json.load(f)

# Making variables in python with information from file
axiom = data['axiom']
rules = data['rules']
alph = data['alph']
trans = data['trans']

# Closing file
f.close()

