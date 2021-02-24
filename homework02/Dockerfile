FROM centos:7.7.1908u

RUN yum update -y && yum install -y python3

ENV LC_CTYPE "en_US.UTF-8"
ENV LANG "en_US.UTF-8"

RUN pip3 install petname==2.6

COPY 3generate_animals.py /code/3generate_animals.py
COPY 3read_animals.py /code/3read_animals.py

RUN chmod +rx /code/3generate_animals.py && \
    chmod +rx /code/read_animals.py

ENV PATH "/code:$PATH"