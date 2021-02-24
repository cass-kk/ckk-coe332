FROM centos:7.7.1908u

RUN yum update -y && yum install -y python3

ENV LC_CTYPE "en_US.UTF-8"
ENV LANG "en_US.UTF-8"

RUN pip3 install petname==2.6

COPY 3generate_animals.py /code/3generate_animals.py
COPY read_animals3.py /code/read_animals3.py

RUN chmod +rx /code/3generate_animals.py && \
    chmod +rx /code/read_animals3.py

ENV PATH "/code:$PATH"