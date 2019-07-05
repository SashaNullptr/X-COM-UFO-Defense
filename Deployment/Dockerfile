FROM ubuntu:18.04

MAINTAINER Sasha Fox "sashanullptr@gmail.com"

RUN apt-get update -y && apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./../requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install ..

COPY .. /app

ENTRYPOINT [ "python" ]

CMD [ "x_com_app.py" ]
