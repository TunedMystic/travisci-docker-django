FROM python:3.6.3-alpine

ENV PYTHONUNBUFFERED="TRUE" APP_PATH="/usr/src/app"

# Install system-level dependencies.
RUN apk update && \
    apk add --virtual \
      build-deps python3-dev

# Make app directories.
RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH

COPY ./requirements.txt $APP_PATH

# Install requirements.txt
RUN pip install -r requirements.txt

ADD . $APP_PATH
