FROM python:3.7-alpine

# RUN apt update
# RUN apt-get install python3-tk

WORKDIR /l-system

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "main.py" ]
