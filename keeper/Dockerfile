FROM ubuntu:16.04
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN apt-get install -y python3-pip
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python", "keeper.py"]
