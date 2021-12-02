#!/bin/sh

DATE=$(date +"%Y-%m-%d-%H:%M:%S") # Make variable DATE with the current date
cp -a ./logs/history.txt "history-$DATE" # Copy the current history.txt file with new name with the DATE varible
mkdir ~/.l-systems/ # Create .l-systems directory in the home directory
mv "history-$DATE" ~/.l-systems/ # Move the new file to the .l-systems in the home directory
