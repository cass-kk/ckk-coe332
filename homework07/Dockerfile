# Image: jstubbs/animals-service
FROM python:3.9

ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN pip install hotqueue

RUN pip install redis

RUN mkdir -p /app

COPY api.py /app

COPY jobs.py /app

COPY worker.py /app

WORKDIR /app

ENTRYPOINT ["python"]

CMD ["api.py", "worker.py"]