# Messaging Systems and Kubernetes

## Part A:

The following commands were used to create the flask and worker deployments, respectively:

```bash
[]$ kubectl apply -f ckk3478-hw7-flask-deployment.yml
```
```bash
[]$ kubectl apply -f ckk3478-hw7-worker-deployment.yml
```

The following curl statements were used to verify that the flask API and worker are correctly working with the respective output/responses returned:

```bash
[]$ curl -X POST -H "content-type: application/json" -d '{"letter1": "A", "letter2": ["b", "B", "bee"]}' 10.100.108.96/<endpoint> 
```
output:
``bash

```

Checking the status of the jobs with:

```bash
[]$
```

And the following is returned as output:

```bash

```


## Part B:

The following code was added to the worker.py file to record the worker's updated IP address:

```python
import os
def execute_job(jid):
  worker_ip = os.environ.get('WORKER_IP')
  job_dict = {'worker ip': worker_ip.decode('utf-8')}
  _save_job(worker_ip, job_dict)
```

## Part C:

The following curl statements to the flask API were used:

```bash
[]$
```

And the respective outputs were recieved

```bash

```

To check the status of the job and the outputs from the statements, the following python code was used:

```python

```

Each worker worked on _____________ jobs.