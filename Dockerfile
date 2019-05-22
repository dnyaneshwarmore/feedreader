FROM ubuntu:18.04
RUN apt-get update 
RUN mkdir feedreader
COPY . feedreader
RUN apt-get install -y python3-pip
RUN pip3 install -r feedreader/requirements.txt 
EXPOSE 8000
CMD ["python3","feedreader/manage.py","runserver","0.0.0.0:8000"]
