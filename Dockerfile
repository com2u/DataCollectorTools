FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y python-dev && \
    apt-get install -y python3-pip && \
    apt-get install -y p7zip-full && \
    apt-get install -y libpq-dev

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app


ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]