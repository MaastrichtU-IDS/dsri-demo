FROM ghcr.io/maastrichtu-ids/openjdk:18

# FROM openjdk:18

# RUN apk add R R-dev R-doc
RUN mkdir -p /app
WORKDIR /app

# TODO: add your jar here
ADD ludii.jar /app

ENTRYPOINT [ "java", "-jar", "/app/ludii.jar" ]
CMD [ "--help" ]