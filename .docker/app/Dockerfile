FROM python:3.8.2-slim

WORKDIR /usr/src/app

LABEL maintainer="onlinejudge95"

COPY requirements.txt .

RUN pip install --requirement requirements.txt

COPY . .

RUN mkdir /etc/gunicorn && \
    mv configs/gunicorn.conf.py /etc/gunicorn/ && \
    mv configs/gunicorn.log.conf /etc/gunicorn/ && \
    rm -rf configs

RUN chmod +x bin/release

ENTRYPOINT [ "./bin/release" ]
