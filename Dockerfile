FROM python:3.10.5-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
  apt-get install -y tesseract-ocr-eng tesseract-ocr libarchive13

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ['python bot.py']
