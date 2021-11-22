FROM ghcr.io/maastrichtu-ids/jupyterlab:latest

# Switch to root user to install packages
USER root

RUN apt update && \
    apt install -y python3-dev libpq-dev

# Switch back to notebook user
USER $NB_USER

ADD . .

RUN pip install -r requirements.txt