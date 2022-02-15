FROM python:3.8

WORKDIR /app

RUN pip install kubernetes openshift-client

ADD *.py /app/

ENTRYPOINT [ "python" ]
CMD [ "kube_controller.py" ]
