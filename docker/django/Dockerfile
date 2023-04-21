FROM python:3.10.11-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# define the application working directory into the container
WORKDIR app

# update the package manager
RUN apk update \
    && apk upgrade

# install all project's dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt /app

COPY ./docker/django/entrypoint.sh /app

RUN pip install -r requirements.txt

# copy the source code into the application working directory
COPY ./src /app

RUN ls
