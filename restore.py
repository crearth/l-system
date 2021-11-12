from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("/home/matias/.l-systems")]
print("available history files for restore:")
for f in onlyfiles:
	print(f)
x = input("What history file would you like to restore? (0 = break loop): ")
print(file)
while x != "0":
	if x in onlyfiles:
		history.txt = open("/home/matias/.l-systems/" + x)
		break
	x = input("What history file would you like to restore? (0= break loop): ")
