FROM alpine/git:v2.32.0 as backendapi
WORKDIR "/root"
RUN mkdir /root/.ssh/
COPY config /root/.ssh/config
COPY volvdev /root/.ssh/id_rsa
RUN chmod -R 400 /root/.ssh && \
 apk add --update py-pip && \
 git clone -b master --single-branch https://github.com/volvtech/volv_dashboard_backend.git \
 pip install awscli && \
 aws configure set aws_access_key_id KKKK && \
 aws configure set aws_secret_access_key HHHH && \
 aws configure set default.region ap-south-1

 FROM python:3.7.12-alpine

 RUN apk update
 
