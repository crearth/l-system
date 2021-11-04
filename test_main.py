from main import getData, getVariables, lSystem
import pytest

# Test the lSystem() function
def test_lSystem():
	iter = 4 
	rules = { "A" : "A+B" , "B" : "A-B" }
	lstring = lSystem("A", rules, iter)
	assert lstring == "A+B+A-B+A+B-A-B+A+B+A-B-A+B-A-B"
