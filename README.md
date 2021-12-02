# l-system
Assignment Informatica Werktuigen (academic year 2021-2022).

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
Run the main.py file.
```bash
python3 main.py
```
It will ask you which configuration file it should use and how many iterations you want. You can find some example configuration files in this repository.

### Configuration file
When you run the main.py file, the program will aks for a configuration file. The configuration file has to be a json file. There is an example.json file in this repository. These are the supported translations:
* angle: turn left
* draw: draw a line
* forward: move forward without drawing a line
* nop: do nothing
* push: push the current drawing state on the stack
* pop: replace the current drawing state with the one on top of the stack
* color: change the color from this point to the given name

with every translation, there is a value or variable:
* angle: amount of degrees
* draw: amount of pixels
* forward: amount of pixels
* nop: value doesn't matter
* push: value doesn't matter
* pop: value doens't matter
* color: name of the color you want, without capitals

### History
A history.txt file will be created in the directory 'logs' when running the main.py for the first time. Every time you run the program, a new line will be added with the configuration information, timestamp and generated l-string.

### History backups
If you wish, you can make backups on a hourly rate with the bash script `backup.sh`. Add the following to your crontab (command crontab -e, replace /path/to/the/project with the path to the project):
```bash
0 * * * * cd /path/to/the/project/ && ./backup.sh >/dev/null 2>&1
``` 

### Restoring a history backup
There is a Python script `restore.py` that you can run if you wish to restore the history database to one of its backups. Simply run the script with the following command:
```bash
python3 restore.py
```
The script will show you all the possible history backups, you have to pick one and the chosen history backup will be copied in place of the current history file.

### Exporting the drawing
Currently, only .eps files are supported.
You can export the drawed l-system with the following command:
```bash
python3 main.py --export <filename>
```
Replace `<filename>` with the name of the file you want, followed by the extension .eps.

### Web server
You can view the information and a svg image of your latest drawing with the following commands:
```bash
export FLASK_APP=webPage
flask run
```
Access the webpage with this url: `http://localhost:5000/index`.

### Docker
You can build a docker image and run a docker container with the project files.
Important: in order for docker to show you the drawing, you should first run the following commands:
#### LINUX
```bash
sudo apt-get install x11-xserver-utils

xhost +
```
#### MACOS (thanks to [this gist](https://gist.github.com/cschiewek/246a244ba23da8b9f0e7b11a68bf3285))
1. install [XQuartz](https://xquartz.org)
2. launch XQuartz, under the XQuartz menu, select Preferences
3. go to security tab and ensure "allow connections from network clients" is checked
4. run the following commands
```bash
xhost + ${hostname}
export HOSTNAME='your_hostname.local'
```

#### Docker container
Then you can start with docker:
```bash
cd /path/to/project

docker build -t l-system:latest

docker run --rm -ti -v ~/.l-system-logs:/logs \
		    -v /tmp/.X11-unix:/tmp/.X11-unix \
                    -e DISPLAY=$DISPLAY \
		    l-system:latest
```
On macOS you should change $DISPLAY to ${HOSTNAME}:0
Now the container will ask you the configuration file and the number of iterations.
