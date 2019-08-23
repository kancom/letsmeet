FROM python:3.7.4

LABEL maintainer="kashirinas@rambler.ru"
LABEL vendor="letsmeet"

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PIPENV_HIDE_EMOJIS=true \
  PIPENV_COLORBLIND=true \
  PIPENV_NOSPIN=true 
  # PIPENV_DOTENV_LOCATION=config/.env


# System deps:

RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        binutils libproj-dev gdal-bin \
        # git \
        # openssh-client \
        libpq-dev \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# RUN apk --no-cache add \
#      bash \
#      build-base \
#      curl \
#      gcc \
#      gettext \
#      # git \
#      # libffi-dev \
#      # linux-headers \
#      # musl-dev \
#      postgresql-dev \
#      tini

# RUN apk --no-cache add \
#     --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
#     --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
#       gdal \
#       py-gdal

# Creating folders, and files for a project:

COPY . /code
WORKDIR /code

# This is a special case. We need to run this script as entry point:
COPY ./docker/entrypoint.sh /docker-entrypoint.sh


# Project initialization:

RUN chmod +x "/docker-entrypoint.sh" \
  && pip install pipenv \
  && pipenv install $(test "$DJANGO_ENV" == production || echo "--dev") --deploy --system --ignore-pipfile

ENTRYPOINT ["/bin/bash", "--", "/docker-entrypoint.sh"]
