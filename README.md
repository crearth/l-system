# l-system
Assignment Informatica Werktuigen (academic year 2021-2022).

## TODO
- [ ] docker
- [ ] comments toevoegen yaml action
- [ ] comments verbeteren getArguments
- [ ] readme uitbreiden

## DONE
- [x] opmaak website (header toegevoegd)
- [x] split draw in functions
- [x] l-system itself
- [x] system history
- [x] checking incorrect input
- [x] extended translations (push, pop, color)
- [x] exporting l-system drawings
- [x] base of web server
- [x] web server: l-system drawings on web server
- [x] configure a CI pipeline
- [x] history file backups
- [x] restoring database from a backup
- [x] unit testing: add 1 history check

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

### History backups
If you wish, you can make backups on a hourly rate with the bash script `backup.sh`. Add the following to your crontab (command crontab -e):
```bash
0 * * * * cd /path/to/the/project/ && ./backup.sh >/dev/null 2>&1
``` 

### Exporting the drawing
Currently, only .eps files are supported.
You can export the drawed l-system with the following command:
```bash
python3 main.py --export <filename>
```
Replace `<filename>` with the name of the file you want, followed by the extension .eps.

### Web server
You can view the information and a picture of your latest drawing with the following command:
```bash
python3 webPage.py
```
Access the webpage with this url: `http://localhost:5000/index`.
