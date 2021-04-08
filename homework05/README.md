# Kubernetes Pods and Deployments

## Part A:

1. Yaml file used: pod-A.yml

To create pod-A.yml:

```bash
[]$ kubectl apply -f pod-A.yml
```

2. Using the selctor function, one can get the pod from its label:

```bash
[]$ kubectl get pods --selector "greeting=personalized"
```
Output:

```bash
NAME    READY   STATUS    RESTARTS   AGE
hello   1/1     Running   0          4m23s
```

3. Check the logs of the pod using kubectl:

```bash
[]$ kubectl logs hello
```
Output:

```bash
Hello, !
```

Yes, this output is expected as the environment name does not have a value associated with it.

4. To delete the pod 'hello':

```bash
[]$ kubectl delete pods hello
```

## Part B:

1. Yaml file used: pod-B.yml

To create pod-B.yml:

```bash
[]$ kubectl apply -f pod-B.yml
```

2. Check the logs of the pod-B.yml file:

```bash
[]$ kubectl logs hello-name
```
Output:

```bash
Hello, Cassandre!
```

3. Delete the pod 'hello-name' with:

```bash
[]$ kubectl delete pods hello-name
```

## Part C:

1. Yaml file used: deployment-C.yml

To create the deployment with three replicas:

```bash
[]$ kubectl apply -f deployment-C.yml
```

2. Getting all of the pods in the deployment as well as their IP addresses:

Using the command:

```bash
[]$ kubectl get pod -o wide
```

Output:

```bash
NAME                                READY   STATUS    RESTARTS   AGE     IP             NODE                         NOMINATED NODE   READINESS GATES
hello-deployment-789bbdd87d-7c8zv   1/1     Running   0          5m39s   10.244.5.122   c04                          <none>           <none>
hello-deployment-789bbdd87d-szg46   1/1     Running   0          5m39s   10.244.3.125   c01                          <none>           <none>
hello-deployment-789bbdd87d-xgwxg   1/1     Running   0          7m41s   10.244.10.12   c009.rodeo.tacc.utexas.edu   <none>           <none>
```

3. Check all of the pods individually with their logs:

Using the following commands:

```bash
[]$ kubectl logs hello-deployment-789bbdd87d-7c8zv
[]$ kubectl logs hello-deployment-789bbdd87d-szg46
[]$ kubectl logs hello-deployment-789bbdd87d-xgwxg
```

And the outputs respectively:

```bash
Hello, Cassandre! from 10.244.5.122
Hello, Cassandre! from 10.244.3.125
Hello, Cassandre! from 10.244.10.12
```

All of the pods match with their IP addresses from the same deployment in number 2.