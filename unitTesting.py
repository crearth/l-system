from main import getData, getVariables, lSystem
import pytest

data = getData("./tests/test1.json")
axiom, rules, variables, constants, trans = getVariables(data)

def test_lSystem(axiom, rules):
	iter = 4 
	lstring = lSystem(axiom, rules, iter)
	assert lstring == "A+B+A-B+A+B-A-B+A+B+A-B-A+B-A-B"
