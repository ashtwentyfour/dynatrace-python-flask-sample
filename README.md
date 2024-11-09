## Flask Application for Dynatrace Kubernetes Workload Testing

* Create Namespace and deploy:

```
$ kubectl create ns flask
```

```
$ kubectl apply -f deployment/flask-sample.yaml -n flask
```

* Validate workload is monitored on Dynatrace under 'Kubernetes > Namespaces > flask' (filter by cluster name)

