FROM python:3.7-alpine

RUN apt update
RUN apt-get install python3-tk

RUN mkdir /l-system/
WORKDIR /l-system
RUN pip install -r requirements.txt
