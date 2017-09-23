FROM python:3

ADD . /
ADD ./helpers /helpers
WORKDIR /

RUN pip3 install -r requirements.txt

CMD [ "python", "./run.py" ]
