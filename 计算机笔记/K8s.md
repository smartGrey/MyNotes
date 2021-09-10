# k8s 

## kubectl

### 常用命令

```bash
kubectl create namespace workspace
kubectl get po --all-namespaces
kubectl delete workspace liu-test-1-42-master --grace-period=0 --force -n workspace
launch -- bash
kubectl get workspace -n workspace
kubectl config set-context --current --namespace=workspace
kubectl get workspace/liu-test1-38 -n workspace -o json
```

