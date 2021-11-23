from main import getData, getVariables, lSystem, addHistory
from datetime import datetime
import pytest

def openFile(file):
	f = open(file,"r")
	return f

# Test the lSystem function with the test1.json
def test_1_lSystem():
	f = openFile("./tests/test1.json")
	data = getData(f)
	axiom, rules, variables, constants, trans = getVariables(data)
	iterations = 4
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == "A+B+A-B+A+B-A-B+A+B+A-B-A+B-A-B"

# Test the lSystem function with the test2.json
def test_2_lSystem():
	f = openFile("./tests/test2.json")
	data = getData(f)
	axiom, rules, variables, constants, trans = getVariables(data)
	iterations = 5
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == "ABAABABAABAAB"

# Test the lSystem function with the binary tree (test3.json)
def test_3_lSystem():
	f = openFile("./tests/test3.json")
	data = getData(f)
	axiom, rules, variables, constants, trans = getVariables(data)
	iterations = 4
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == "11111111+[1111+[11+[1+[0-]0-]1+[0-]0-]11+[1+[0-]0-]1+[0-]0-]1111+[11+[1+[0-]0-]1+[0-]0-]11+[1+[0-]0-]1+[0-]0"

# Test the lSystem function with the example of the assignment (test4.json)
def test_4_lSystem():
	f = openFile("./tests/test4.json")
	data = getData(f)
	axiom, rules, variables, constants, trans = getVariables(data)
	iterations = 3
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == "AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]+[+AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]-AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]-AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]]-[-AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]+AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]+AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]]"

# Test the lSystem function with tests5.json
def test_5_lSystem():
	f = openFile("./tests/test5.json")
	data = getData(f)
	axiom, rules, variables, constants, trans = getVariables(data)
	iterations = 3
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == "F-G+F+G-F-GG+F-G+F+G-F+GG-F-G+F+G-F-GGGG+F-G+F+G-F-GG+F-G+F+G-F+GG-F-G+F+G-F+GGGG-F-G+F+G-F-GG+F-G+F+G-F+GG-F-G+F+G-F-GGGGGGGG-GGGGGGGG"

def test_4_hisotry():
	f = openFile("./tests/test4.json")
	data = getData(f)
	axiom, rules, variables, constants, trans = getVariables(data)
	iterations = 5
	timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	lstring = lSystem(axiom, rules, iterations)
	history = addHistory(axiom, rules, trans, iterations, lstring, variables, constants)
	correctHistory = timestamp + "\t" + str(variables) + "\t" + str(constants) + "\t" + axiom + "\t" + str(rules) + "\t" + str(trans) + "\t" + str(iterations) + "\t" + str(lstring) + "\n" 
	assert history == correctHistory

# Test the history file write function
def test_3_hisotry():
	f = openFile("./tests/test3.json")
	data = getData(f)
	axiom, rules, variables, constants, trans = getVariables(data)
	iterations = 4
	timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	lstring = lSystem(axiom, rules, iterations)
	history = addHistory(axiom, rules, trans, iterations, lstring, variables, constants)
	correctHistory = timestamp + "\t" + str(variables) + "\t" + str(constants) + "\t" + axiom + "\t" + str(rules) + "\t" + str(trans) + "\t" + str(iterations) + "\t" + str(lstring) + "\n" 
	assert history == correctHistory
