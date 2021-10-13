FROM python:3.9.7-bullseye
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt
COPY . .

EXPOSE 5000