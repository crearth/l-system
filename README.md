# l-system
Assignment Informatica Werktuigen (academic year 2021-2022).

## TODO
	* complete unit testing with pytest
	* configure a CI pipeline
	* history file backups
	* web server: l-system drawings on web server
	* docker
## DONE
	* l-system itself
	* system history
	* checking incorrect input
	* extended translations (push, pop, color)
	* exporting l-system drawings
	* base of web server

## Installation
Clone this repository to your local computer.
```bash
git clone https://github.com/crearth/l-system.git
```

Configure a python virtual environment with [venv](https://docs.python.org/3/library/venv.html).
```bash
python3 -m venv l-venv
```

Use the virtual environment.
```bash
source l-venv/bin/activate
```

Install the packages via pip.
```bash
pip install -r requirements.txt
```

Install the tkinter package.
```bash
sudo apt-get install python3-tk
```

## Use
Run the main.py file. It will ask you wich configuration file it should use and how many iterations you want. You can find some example configuration files in this repository.

### Configuration file
When you run the main.py file, the program will aks for a configuration file. The configuration file has to be a json file. There is an example.json file in this repository. These are the supported translations:
	* angle: turn 
	* draw: draw a line
	* forward: move forward without drawing a line
	* nop: do nothing
	* push: push the current drawing state on the stack
	* pop: replace the current drawing state with the one on top of the stack
	* color: change the color from this point to the given name

### History
A history.txt file will be created when running the main.py for the first time. Every time you run the program, a new line will be added with the configuration information and timestamp.  

### Exporting the drawing
Currently, only .eps files are supported.
You can export the drawed l-system with the following command:
```bash
python3 main.py --export <filename>
```
Replace `<filename>` with the name of the file you want, followed by the extension .eps.

### Web server
You can view the information of your latest drawing with the following command:
```bash
python3 webPage.py
```
