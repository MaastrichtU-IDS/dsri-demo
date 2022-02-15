We use the project `controlling-kube` by default, replace it in all file in this folder by your project name. And go to your project:

```bash
oc project your-project
```

## Grant kubernetes API permission

⚠️ You will need admin permission in the cluster to create the roles and permissions:

```bash
oc apply -f roles.yml
```

## Use a workspace

Install [Helm](https://helm.sh/docs/intro/install/)

<details><summary>Install the Helm repository locally if not already done</summary>

```bash
helm repo add dsri https://maastrichtu-ids.github.io/dsri-helm-charts/
helm repo update
```
</details>

Start the JupyterLab/VSCode workspace in your DSRI project:

```bash
helm install workspace dsri/jupyterlab \
  --set serviceAccount.name=kube-controller \
  --set service.openshiftRoute.enabled=true \
  --set image.tag=latest \
  --set storage.mountPath=/home/jovyan/work \
  --set gitUrl=https://github.com/MaastrichtU-IDS/dsri-demo \
  --set password=changeme
```

Install the dependencies in your workspace terminal:

```bash
pip install kubernetes openshift-client
```

Uninstall the chart:

```bash
helm uninstall workspace
```

## Run a job

Create the ImageStream (to do once)

```bash
oc new-build --name pykube-controller --binary
```

Build the image defined in this local folder on the cluster (to re-execute everytime you make changes to the python script)

```bash
oc start-build pykube-controller --from-dir=. --follow --wait
```

Optionally you can run the script as a job, start the job:

```bash
oc apply -f job.yml
```

Get the jobs logs:

```bash
oc logs job/pykube-controller
```

Delete the job (before re-running it):

```bash
oc delete -f job.yml
```

