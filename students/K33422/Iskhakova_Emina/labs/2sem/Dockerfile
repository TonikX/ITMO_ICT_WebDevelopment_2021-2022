FROM python:3.8.5

RUN apt update && apt upgrade -y && apt autoclean

RUN mkdir /project
COPY . /project/
WORKDIR /project

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
