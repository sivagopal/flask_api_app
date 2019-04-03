# our base image
FROM alpine:latest

USER root

RUN mkdir /my_app

WORKDIR /my_app

# install Python modules needed by the Python app
COPY requirements.txt /my_app

RUN pwd

RUN ls -la

RUN apt-get update

RUN apt-get install -y python-pip

# copy files required for the app to run
COPY app.py /my_app

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/my_app/app.py"]
