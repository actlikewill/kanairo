FROM python:3.8-alpine

LABEL application="kanairo-backend"

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apk add --no-cache python3 postgresql-libs && \
    apk add --no-cache --virtual .build-deps libffi-dev \
       gcc python3-dev musl-dev postgresql-dev build-base jpeg-dev zlib-dev

COPY ./requirements.txt /code/

COPY ./entrypoint.sh /code/

RUN chmod +x *.sh

RUN pip install -r requirements.txt

COPY . /code/