# Kubernetes Confluent demo apps

You'll need:

* Bootstrap Server
* Confluent API Key
* Confluent Secret Key

Create a namespace:

```
kubectl create ns demo
```

Create a secret containing the items above:
```
kubectl create secret generic nr-confluent-secrets --from-literal=bootstrap-server=<your bootstrap server> --from-literal=api-key=<your api key> --from-literal=secret-key=<your secret key> -n demo
```

Deploy apps:
```
kubectl create -f . -n demo
```
