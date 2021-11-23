# Import needed library
from flask import Flask, render_template

# Set app
app = Flask(__name__)
# Get last line of history.txt file
with open("history.txt", "r") as f:
	last_line = f.readlines()[-1]

split = last_line.split("\t") # Split last_line in list were there was a tab in between
# Get needed variables from split
time = split[0]
variables = split[1]
constants = split[2]
axiom = split[3]
rules = split[4]
trans = split[5]
iterations = split[6]
lstring = split[7]
svgFile = open("./static/.lstring.svg", "r")
svgText = svgFile.read()

# Define /index page
@app.route("/index")
def home():
	# Use index.html as html code for the website and pass in needed variables as arguments
	return render_template("index.html", timestamp=time, variables=variables, constants=constants, axiom=axiom, rules=rules, translations=trans, iterations=iterations, endstring=lstring, svgText=svgText)

if __name__ == "__main__":
	app.run()
