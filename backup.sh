#!/bin/sh

DATE=$(date +"%Y-%m-%d-%H_%M_%S")
cp -a history.txt "history-$DATE"
mv "history-$DATE" ~/.l-systems/
