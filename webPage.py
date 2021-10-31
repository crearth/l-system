from flask import Flask, render_template

app = Flask(__name__)
with open("history.txt", "r") as f:
	last_line = f.readlines()[-1]

split = last_line.split("\t")
time = split[0]
variables = split[1]
constants = split[2]
axiom = split[3]
rules = split[4]
trans = split[5]
iterations = split[6]
lstring = split[7]

@app.route("/")
def home():
	return render_template("index.html", timestamp=time, variables=variables, constants=constants, axiom=axiom, rules=rules, traslations=trans, iterations=iterations, endstring=lstring)

if __name__ == "__main__":
	app.run()

