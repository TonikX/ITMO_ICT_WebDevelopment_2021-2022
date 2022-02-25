FROM python:3.9

RUN apt-get update -y && apt-get upgrade -y
RUN python -m pip install --upgrade pip setuptools

RUN mkdir /app
WORKDIR /app

# Python dependencies
COPY requirements* ./
RUN pip install -r requirements_production.txt

# We copy the rest of the codebase into the image
COPY . .
WORKDIR /app/check_splitter
