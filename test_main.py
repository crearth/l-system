from main import getData, getVariables, lSystem, addHistory
from datetime import datetime
import pytest

# Test the lSystem function with the test1.json
def test_1_lSystem():
	iterations = 4
	axiom = "A"
	rules = { "A" : "A+B" , "B" : "A-B" }
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == "A+B+A-B+A+B-A-B+A+B+A-B-A+B-A-B"

# Test the lSystem function with the test2.json
def test_2_lSystem():
	iterations = 5
	axiom = "A"
	rules = { "A" : "AB" , "B" : "A" }
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == "ABAABABAABAAB"

# Test the lSystem function with the binary tree (test3.json)
def test_3_lSystem():
	iterations = 4
	axiom = "0"
	rules = { "1" : "11" , "0" : "1+[0-]0" }
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == "11111111+[1111+[11+[1+[0-]0-]1+[0-]0-]11+[1+[0-]0-]1+[0-]0-]1111+[11+[1+[0-]0-]1+[0-]0-]11+[1+[0-]0-]1+[0-]0"

# Test the lSystem function with the example of the assignment (test4.json)
def test_4_lSystem():
	iterations = 3
	axiom = "A"
	rules = { "A" : "AA+[+A-A-A]-[-A+A+A]" }
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == "AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]+[+AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]-AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]-AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]]-[-AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]+AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]+AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]]"

# Test the lSystem function with tests5.json
def test_5_lSystem():
	iterations = 3
	axiom = "F-G-G"
	rules = { "F" : "F-G+F+G-F", "G" : "GG" }
	lstring = lSystem(axiom, rules, iterations)
	assert lstring == "F-G+F+G-F-GG+F-G+F+G-F+GG-F-G+F+G-F-GGGG+F-G+F+G-F-GG+F-G+F+G-F+GG-F-G+F+G-F+GGGG-F-G+F+G-F-GG+F-G+F+G-F+GG-F-G+F+G-F-GGGGGGGG-GGGGGGGG"

# Test the history file write function
def test_3_hisotry():
	iterations = 4
	axiom = "0"
	rules = { "1" : "11" , "0" : "1+[0-]0" }
	variables = ["0", "1"]
	constants = ["[" , "]", "+" , "-"]
	trans = { "0" : ["draw", 2] , "1" : ["draw" , 2] , "[" : ["angle", 45] , "]" : ["angle" , -45] , "+" : ["push" , 1] , "-" : ["pop" , 1] }
	timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	lstring = lSystem(axiom, rules, iterations)
	history = addHistory(axiom, rules, trans, iterations, lstring, variables, constants)
	correctHistory = timestamp + "\t" + str(variables) + "\t" + str(constants) + "\t" + axiom + "\t" + str(rules) + "\t" + str(trans) + "\t" + str(iterations) + "\t" + str(lstring) + "\n" 
	assert history == correctHistory
