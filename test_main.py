from main import getData, getVariables, lSystem
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
