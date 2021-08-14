FROM python:3.7.11-slim-buster

ENV APP_DIR=/opt/app

SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]

# hadolint ignore=DL3008
RUN apt-get update -qq -y \
    && apt-get install --no-install-recommends -qq -y \
        build-essential \
        gosu \
        libpcre3 \
        libpcre3-dev \
        curl \
        unzip \
    && apt-get -y autoclean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR ${APP_DIR}
COPY data data/

# Download word embeddings
RUN curl -O http://neuroner.com/data/word_vectors/glove.6B.100d.zip \
    && rm -fr data/word_vectors/* \
    && unzip glove.6B.100d.zip -d data/word_vectors

COPY requirements.txt prod-requirements.txt uwsgi.ini ./
RUN pip install --no-cache-dir \
    -r requirements.txt -r prod-requirements.txt \
    # Install spacy assets required by NeuroNER
    && python -m spacy download en_core_web_sm \
    # Create folder required by NeuroNER
    && mkdir -p output

COPY openapi_server openapi_server/
# Create the user used by uWSGI to run the tool
RUN useradd --create-home --shell /bin/bash nlp \
    && chown -R nlp:nlp ${APP_DIR}

WORKDIR /
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/docker-entrypoint.sh"]

# Run server in development mode
# CMD ["python", "-m", "openapi_server"]

# Run server in production mode
CMD ["uwsgi", "--ini", "uwsgi.ini", "--lazy", "--http", ":8080"]