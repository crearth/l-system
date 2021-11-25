# getting base image of Ubuntu 18.04
FROM ubuntu:18.04

# we do not want the apt-get install asking questions
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install \
	python \
	python3 \
	python-pip \
	python3-pip \
	python3-markupsafe \
	python-tk \
	python3-tk \
	ghostscript

COPY requirements.txt /l-system/

WORKDIR /l-system

RUN pip3 install -r requirements.txt

COPY . /l-system

ENV FLASK_APP webPage

CMD [ "python3", "main.py" ]
#CMD ["bash"]
