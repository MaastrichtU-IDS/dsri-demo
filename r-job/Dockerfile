FROM alpine:3.15
RUN apk add R R-dev R-doc
RUN mkdir -p /app
WORKDIR /app
ADD rcode.r /app
CMD ["Rscript", "--no-save", "/app/rcode.r"] 
