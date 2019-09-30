# feedreader
Application can be set up using 2 ways
1) Directly run as docker image (created and pushed to dockerhub)
2) Setup all required libraries on os and then run
Steps to run application using docker image.
Note:- please have docker installed on your system ( ubuntu )
1) Pull the docker image (don’t have any cloud account hence used docker)
sudo docker pull maulimore/feedreader:latest
2) run the docker image
sudo docker run -id -p 8000:8000 maulimore/feedreader:latest
3) access the UI
Open browser and hit “http://localhost:8000/processor”
Steps to run project directly on os (prefer ubuntu as all development is done on ubuntu
only.
Note: must have python3 installed on the system.
1) Extract the given compressed file
2) Open terminal and change working directory to extracted folder
3) Install required packages and libraries
● sudo apt-get update
● apt-get install -y python3-pip
● pip3 install -r feedreader/requirements.txt
4) run the project to access it.
Python3 manage.py runserver
5) access the UI
Open browser and hit “http://localhost:8000/processor”
Project is tested against url “http://feeds.bbci.co.uk/news/rss.xml”
