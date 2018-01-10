FROM python:3.6.4-alpine3.7

MAINTAINER Mathias Schilling <m@matchilling.com>

ENV APP_PATH /usr/src/mrjob

# Install modules
RUN apk add --update bash && \
    apk add --update openssh && \
    rm -rf /var/cache/apk/*

# Create ssh directory
RUN mkdir -p ~/.ssh

# Create app directory
RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH

# Install app dependencies
COPY . $APP_PATH
RUN pip install --no-cache-dir -r docker/mrjob/requirements.txt

VOLUME $APP_PATH

CMD [ "/bin/sh" ]
