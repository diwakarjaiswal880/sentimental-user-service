FROM python:3.8.2-slim

LABEL maintainer="onlinejudge95"

WORKDIR /usr/src/app

# RUN groupadd -g 999 appuser && \
#     useradd -r -u 999 -g appuser appuser

# USER appuser

COPY requirements.txt .

RUN pip install --requirement requirements.txt

COPY . .

RUN mkdir /etc/gunicorn && \
    mv configs/gunicorn.conf.py /etc/gunicorn/ && \
    mv configs/gunicorn.log.conf /etc/gunicorn/ && \
    rm -rf configs

RUN chmod +x bin/release

ENTRYPOINT [ "./bin/release" ]
