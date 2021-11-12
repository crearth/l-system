from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("/home/matias/.l-systems")]
print("available history files for restore:")
for f in onlyfiles:
	print(f)
f = input("What history file would you like to restore? (0 = break loop): ")
file = open("/home/matias/.l-systems/" + f)
while f != "0":
	if f in onlyfiles:
		history = open("history.txt", "r+")
		history.truncate(0)
		content = file.read()
		history.write(content)
		history.close
		break
	f = input("What history file would you like to restore? (0= break loop): ")
