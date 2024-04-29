# s3fs-sidecar issue

OCP 4.12.44 / ODF 4.12.12

```bash
$ podman build -t s3image-fedora .
$ podman tag localhost/s3image quay.io/jclaret/s3image-fedora
$ podman push quay.io/jclaret/s3image-fedora

$ oc new-project s3-testing
$ oc create -f 01-ObjectBucketClaim.yaml
$ oc get ocm
$ oc get secret
$ oc create -f 02-sample.yaml - change S3URL / AWSACCESSKEYID / AWSSECRETACCESSKEY / BUCKET

$ oc get pod
NAME        READY   STATUS    RESTARTS   AGE
sample-s3   2/2     Running   0          7m

$ oc logs sample-s3 -c debian-container -f

$ oc logs noobaa-endpoint-5dbc555d8-gmmzh -n openshift-storage -f
```
