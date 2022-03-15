FROM python:3.10.1

WORKDIR /app
ENV PYTHONPATH=/app

RUN pip install --upgrade pip
COPY ./requirements/base.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app
