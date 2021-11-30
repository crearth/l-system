from main import getData, getVariables, lSystem, addHistory
from datetime import datetime
import pytest

def openFile(file):
	f = open(file,"r")
	return f

def getResult(file):
	f = openFile("./tests/results.json")
	data = getData(f)
	return data[file]

# Test the lSystem function with the test1.json
def test_1_lSystem():
	f = openFile("./tests/test1.json")
	data = getData(f)
	axiom, rules, variables, constants, trans = getVariables(data)
	iterations = 4
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == getResult("test1.json")

# Test the lSystem function with the test2.json
def test_2_lSystem():
	f = openFile("./tests/test2.json")
	data = getData(f)
	axiom, rules, variables, constants, trans = getVariables(data)
	iterations = 5
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == getResult("test2.json")

# Test the lSystem function with the binary tree (test3.json)
def test_3_lSystem():
	f = openFile("./tests/test3.json")
	data = getData(f)
	axiom, rules, variables, constants, trans = getVariables(data)
	iterations = 4
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == getResult("test3.json")

# Test the lSystem function with the example of the assignment (test4.json)
def test_4_lSystem():
	f = openFile("./tests/test4.json")
	data = getData(f)
	axiom, rules, variables, constants, trans = getVariables(data)
	iterations = 3
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == getResult("test4.json")

# Test the lSystem function with tests5.json
def test_5_lSystem():
	f = openFile("./tests/test5.json")
	data = getData(f)
	axiom, rules, variables, constants, trans = getVariables(data)
	iterations = 3
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == getResult("test5.json")

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
