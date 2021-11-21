# getting base image of Ubuntu 18.04
FROM ubuntu:18.04

# we do not want the apt-get install asking questions
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install \
	python3 \
	python3-pip \
	python3-markupsafe \
	python3-tk \
	cmake \
	ghostscript \
	git \
	libffi-dev \
	libfreetype6-dev \
	libfribidi-dev \
	libharfbuzz-dev \
	libjpeg-turbo-progs \
	libjpeg8-dev \
	liblcms2-dev \
	libopenjp2-7-dev \
	libssl-dev \
	libsqlite3-dev \
	libtiff5-dev \
	libwebp-dev \
	netpbm \
	sudo \
	tcl8.6-dev \
	tk8.6-dev \
	wget \
	xvfb \
	zlib1g-dev \
	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt /l-system/

WORKDIR /l-system

RUN pip3 install -r requirements.txt

COPY . /l-system

#CMD [ "python3", "main.py" ]
CMD ["bash"]
