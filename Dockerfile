FROM python:3.8-slim

COPY ./entrypoint.sh /entrypoint.sh
COPY ./app /app
COPY ./requirements.txt /requirements.txt

#RUN python3 -m pip install -r /requirements.txt   can't do directly before installing with apt-get

RUN apt-get update && \
 apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    tesseract-ocr \
    make \
    gcc


RUN python3 -m pip install -r /requirements.txt  \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

RUN chmod +x /entrypoint.sh

CMD ["entrypoint.sh"]