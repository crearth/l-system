# Import needed librarys
from os import listdir, remove
from os.path import isfile, join
import getpass

# Set username that we will later use to acces .l-systems
username = getpass.getuser()

# Onlyfiles is the variables in .l-system
onlyfiles = [f for f in listdir("/home/" + str(username) + "/.l-systems")]
print("available history files for restore:")

# Print all available history files
for f in onlyfiles:
	print(f)

f = input("What history file would you like to restore? (0 = break loop): ")

while f != "0": # User can give "0" as input to stop program
	if f in onlyfiles: # If the input is in the onlyfiles

		history = open("./logs/history.txt", "r+") # Open history file
		backup = open("/home/" + str(username) + "/.l-systems/" + f) # Open backup file
		history.truncate(0) # Delete content of history.txt
		content = backup.read() # Read content of backup file
		history.write(content) # Write backup content in history.txt
		history.close() # Close history file
		backup.close() # Close backup file
		svg = open("./static/.lstring.svg", "w")
		svg.write('<svg height="30" width="300"> <text x="0" y="15" fill="red">You restored the history, there is no image.</text> </svg>') # Replaces the svg so it doesn't show up on the webpage
		break
	f = input("What history file would you like to restore? (0 = break loop): ")
