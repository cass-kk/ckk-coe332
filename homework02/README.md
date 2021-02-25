# Dr. Moreau Containers
This project builds upon two already written python scripts that uses the petname library to generate and print random animals.  A new additional feature is randomly choosing two of the created animals (parent animals) and breeding them to get the offspring.  Each feature of the offspring is randomly chosen either from parent 1 or parent 2 (except for the tail which is the numerical value of the addition of the arms and legs).

## Installation

To clone the repository:

```bash
[]$ git clone https://github.com/cass-kk/ckk-coe332/homework02
```

## Running the Code

To run the code on the command line:

NOTE: need to have the following with open() to run on the command line
in 3generate_animals.py

```python
   with open('3animals.json', 'w') as out:
   	json.dump(dict_animals, out, indent=2)
```
and in read_animals3.py

```python
   with open('3animals.json', 'r') as f:
   	dict_animals = json.load(f)
```

```bash
[]$ python3 3generate_animals.py
```

A new file, 3animals.json is created.  Then, to print out an animal at random and the offspring of two random animals:

```bash
[]$ python3 read_animals3.py
```

To run the unit test on the breed function in the read_animals3.py file:

```bash
[]$ python3 test_read_animals.py
```

## Docker Image

For the python scripts to work, ensure that both the python3 and petname packages are installed:

```bash
[root@]# yum install python3
[root@]# python3 --version
Python 3.6.8
[root@]# pip3 install petname==2.6
```

If a UnicodeDecodeError appears from the pip3 install:

```bash
[root@]# export LC_CTYPE=en_US.UTF-8
[root@]# export LANG=en_US.UTF-8
[root@]# pip3 install petname
```

Installing the scripts into a container:

```bash
[root@]# cd /code
[root@]# chmod +rx 3generate_animals.py
[root@]# chmod +rx read_animals3.py
[root@]# export PATH=/cod:$PATH
```

Test the code inside the container:

```bash
[root@]# cd /home
[root@]# 3generate_animals.py 3animals.json
[root@]# ls
[root@]# read_animals3.py 3animals.json
```

To build the Docker image:

```bash
[]$ docker build -t <dockerhubusername>/<code_name>:<version> .
```

NOTE: Do NOT forget the period at the end of the previous command line

## Test the Docker image:

INTERACTIVELY:

```bash
[]$ docker run --rm -it username/<code_name>:<version> /bin/bash
[root@]# ls /code
[root@]# cd /home
[root@ home]# 3generate_animals.py test.json
[root@ home]# read_animals3.py test.json
```bash

NON-INTERACTIVELY:

```bash
[]$ mkdir test
[]$ cd test
[]$ docker run --rm -v $PWD:/data -u $(id -u):$(id -g) username/<code_name>:<version> 3generate_animals.py /data/animals.json
[]$ docker run --rm -v $PWD:/data username/<code_name>:<version> read_animals3.py /data/animals.json
```