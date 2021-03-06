This folder explains how to prepare a DSRI project to run Java scripts as jobs. As seen in https://maastrichtu-ids.github.io/dsri-documentation/docs/deploy-rstudio

To try it yourself, first clone the repository and go to this folder with your terminal:

```bash
git clone https://github.com/MaastrichtU-IDS/dsri-demo.git
cd dsri-demo/java-job
```

Make sure you are in the right project on the DSRI:

```bash
oc project $YOUR_PROJECT
```

## Prepare the volume

Create the volume (will be mounted on `/data` in the containers):

```bash
oc apply -f volume.yml
```

Start the Ubuntu container that will be used to copy the data generated by the jobs:

```bash
oc apply -f copy-container.yml
```

## Run the job

Create the image in your project (to do only once):

```bash
oc new-build --name java-job --binary
```

Build the docker image on the DSRI (to re-run everytime you make a change to the script and content of the docker image):

```bash
oc start-build java-job --from-dir=. --follow --wait
```

Start the job:

```bash
oc apply -f job.yml
```

Get the jobs logs:

```bash
oc logs job/java-job
```

Copy the files produced by the job in `/data` on the DSRI to a `data` folder in your current local folder:

```bash
oc get pod --selector app=java-job --no-headers -o=custom-columns=NAME:.metadata.name | xargs -I {} oc cp {}:/data ./data
```

Delete the job (before re-running it):

```bash
oc delete -f job.yml
```

Delete everything (including the persistent volume and the copy-container)

```bash
oc delete all,pvc,secret,configmaps,serviceaccount,rolebinding --selector app=java-job
```

## Notes

Make sure the R script write the output to the persistent volume, in our case `/data` in the container.

You can also start an application like JupyterLab or the filebrowser instead of Ubuntu in `copy-container.yml` to browse the output files using a web UI.