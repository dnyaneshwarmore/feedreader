FROM ubuntu:18.04
RUN apt-get update && apt-get -y upgrade --fix-missing
RUN mkdir feedreader
COPY . feedreader
RUN apt-get install -y python3-pip
RUN pip3 install -r feedreader/requirements.txt 
CMD ["python3","feedreader/manage.py","runserver","0.0.0.0:8000"]
