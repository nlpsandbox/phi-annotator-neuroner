[![nlpsandbox.io](https://nlpsandbox.github.io/nlpsandbox-themes/banner/Banner@3x.png)](https://nlpsandbox.io)

# NeuroNER NLP Sandbox PHI Annotator

[![GitHub Release](https://img.shields.io/github/release/nlpsandbox/phi-annotator-neuroner.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/phi-annotator-neuroner/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/nlpsandbox/phi-annotator-neuroner/CI.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/phi-annotator-neuroner/actions)
[![GitHub License](https://img.shields.io/github/license/nlpsandbox/phi-annotator-neuroner.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/phi-annotator-neuroner/blob/main/LICENSE)
[![Docker](https://img.shields.io/badge/docker-blue.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=nlpsandbox&logo=data:image/svg%2bxml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJtMy4yIDcuOS0xLjctMXYxMS40bDkuOSA1LjdWMTIuNkw1LjYgOS4zIDMuMiA3Ljl6bTE3LjEtMS4zIDEuNS0uOUwxMiAwIDIuMiA1LjdsMi42IDEuNS4xLjEgMS43IDEgNS41IDMuMiA1LjEtMyAzLjEtMS45ek0xMiA5LjUgOS4zIDcuOSA3LjQgNi44bC0xLjctMS0uMS0uMWgtLjFMMTIgMS45bDYuNSAzLjhMMTYuMyA3IDEyIDkuNXptOC44LTEuNi0yLjQgMS40LS41LjItNS4zIDMuMVYyNGw5LjktNS43VjYuOWwtMS43IDF6IiBmaWxsPSIjZmZmIi8+PC9zdmc+)](https://www.synapse.org/#!Synapse:syn26056768 "Get the Docker image of this tool on NLPSandbox.io")
[![Leaderboard](https://img.shields.io/badge/leaderboard-blue.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=nlpsandbox&logo=data:image/svg%2bxml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJtMy4yIDcuOS0xLjctMXYxMS40bDkuOSA1LjdWMTIuNkw1LjYgOS4zIDMuMiA3Ljl6bTE3LjEtMS4zIDEuNS0uOUwxMiAwIDIuMiA1LjdsMi42IDEuNS4xLjEgMS43IDEgNS41IDMuMiA1LjEtMyAzLjEtMS45ek0xMiA5LjUgOS4zIDcuOSA3LjQgNi44bC0xLjctMS0uMS0uMWgtLjFMMTIgMS45bDYuNSAzLjhMMTYuMyA3IDEyIDkuNXptOC44LTEuNi0yLjQgMS40LS41LjItNS4zIDMuMVYyNGw5LjktNS43VjYuOWwtMS43IDF6IiBmaWxsPSIjZmZmIi8+PC9zdmc+)](https://www.synapse.org/#!Synapse:syn22277123/wiki/608544 "View the performance of this tool on NLPSandbox.io")
[![Discord](https://img.shields.io/discord/770484164393828373.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=Discord&logo=discord)](https://nlpsandbox.io/discord "Realtime support / chat with the community and the team")

## Introduction

[NLPSandbox.io] is an open platform for benchmarking modular natural language
processing (NLP) tools on both public and private datasets. Academics, students,
and industry professionals are invited to browse the available tasks and
participate by developing and submitting an NLP Sandbox tool.

This repository packages [NeuroNER] as an [NLP Sandbox PHI annotator]. The
performance of this tool can be viewed and compared to the performance of other
PHI annotators on [NLPSandbox.io].

Annotations supported by NeuroNER:

Annotation  | Schema                     | Supported
------------|----------------------------|----------
Contact     | [TextContactAnnotation]    | Yes
Date        | [TextDateAnnotation]       | Yes
ID          | [TextIdAnnotation]         | Yes
Location    | [TextLocationAnnotation]   | Yes
Person Name | [TextPersonNameAnnotation] | No


## Table of contents

- [Specification](#Specification)
- [Requirements](#Requirements)
- [Usage](#Usage)
  - [Running with Docker](#Running-with-Docker)
  - [Running with Python](#Running-with-Python)
  - [Accessing the user interface](#Accessing-the-user-interface)
- [Development](#Development)
- [Versioning](#Versioning)
  - [GitHub release tags](#GitHub-release-tags)
  - [Docker image tags](#Docker-image-tags)
- [Benchmarking on NLPSandbox&#46;io](#Benchmarking-on-NLPSandbox&#46;io)
- [Citation](#Citation)
- [Contributing](#Contributing)
- [License](#License)


## Specification

- NLP Sandbox tool version: 1.0.0
- NLP Sandbox schemas version: 1.2.0
- Docker image: [docker.synapse.org/syn22277123/phi-annotator-neuroner]


## Requirements

- [Docker Engine] >=19.03.0


## Usage

### Running with Docker

The command below starts this NLP Sandbox PHI annotator locally.

```console
docker compose up --build
```

You can stop the container run with `Ctrl+C`, followed by `docker compose down`.

### Running with Python

Create a Conda environment.

```console
conda create --name phi-annotator-neuroner python=3.7 -y
conda activate phi-annotator-neuroner
```

> Note: NeuroNER only support up to Python 3.7.

Download the word embeddings file (too large to be tracked on GitHub).

```
curl -O http://neuroner.com/data/word_vectors/glove.6B.100d.zip
unzip glove.6B.100d.zip -d server/data/word_vectors/
```

Install and start this NLP Sandbox tool.

```console
cd server && pip install -r requirements.txt
python -m openapi_server
```

### Accessing the user interface

This NLP Sandbox tool provides a web interface that you can use to annotate
clinical notes. This web client has been automatically generated by
[openapi-generator]. To access the UI, open a new tab in your browser and
navigate to one of the following address depending on whether you are running
the tool using Docker (production) or Python (development).

- Using Docker: http://localhost/ui
- Using Python: http://localhost:8080/ui


## Development

Please refer to the section `Development` of the [NLP Sandbox PHI Annotator
example] for information on how to develop an NLP Sandbox PHI annotator in
Python-Flask and other programming languages-frameworks.


## Versioning

### GitHub release tags

This repository uses [semantic versioning] to track the releases of this tool.
This repository uses "non-moving" GitHub tags, that is, a tag will always point
to the same git commit once it has been created.

### Docker image tags

The artifact published by the [CI/CD workflow] of this GitHub repository is a
Docker image pushed to the Synapse Docker Registry. This table lists the image
tags pushed to the registry.

| Tag name                    | Moving | Description
|-----------------------------|--------|------------
| `latest`                    | Yes    | Latest stable release.
| `edge`                      | Yes    | Latest commit made to the default branch.
| `edge-<sha>`                | No     | Same as above with the reference to the git commit.
| `<major>.<minor>.<patch>`   | No     | Stable release.

You should avoid using a moving tag like `latest` when deploying containers in
production, because this makes it hard to track which version of the image is
running and hard to roll back.


## Benchmarking on NLPSandbox&#46;io

Visit [nlpsandbox.io] for instructions on how to submit your NLP Sandbox tool
and evaluate its performance.


## Citation

- If you use NeuroNER in your publications, please follow the [citation
  guidelines given by the authors of NeuroNER].
- If you use this NLP Sandbox tool or resources from [NLPSandbox.io], please
  follow these [citation guidelines].


## Contributing

Thinking about contributing to this project? Get started by reading our
[contribution guide].


## License

[Apache License 2.0]

<!-- Links -->

[nlpsandbox.io]: https://www.synapse.org/nlpsandbox
[Synapse.org]: https://synapse.org
[openapi-generator]: https://github.com/OpenAPITools/openapi-generator
[contribution guide]: .github/CONTRIBUTING.md
[Apache License 2.0]: https://github.com/nlpsandbox/phi-annotator-neuroner/blob/main/LICENSE
[Docker Engine]: https://docs.docker.com/engine/install/
[CI/CD workflow]: .github/workflows/ci.yml
[semantic versioning]: https://semver.org/
[NeuroNER]: https://github.com/Franck-Dernoncourt/NeuroNER
[NLP Sandbox PHI annotator]: https://www.synapse.org/#!Synapse:syn22277123/wiki/609134
[docker.synapse.org/syn22277123/phi-annotator-neuroner]: https://www.synapse.org/#!Synapse:syn26056768
[NLP Sandbox PHI Annotator example]: https://github.com/nlpsandbox/phi-annotator-example
[citation guidelines given by the authors of NeuroNER]: https://github.com/Franck-Dernoncourt/NeuroNER#citation
[citation guidelines]: https://www.synapse.org/#!Synapse:syn22277123/wiki/609146
[TextContactAnnotation]: https://github.com/nlpsandbox/nlpsandbox-schemas/blob/main/openapi/commons/components/schemas/TextContactAnnotation.yaml
[TextDateAnnotation]: https://github.com/nlpsandbox/nlpsandbox-schemas/blob/main/openapi/commons/components/schemas/TextDateAnnotation.yaml
[TextIdAnnotation]: https://github.com/nlpsandbox/nlpsandbox-schemas/blob/main/openapi/commons/components/schemas/TextIdAnnotation.yaml
[TextLocationAnnotation]: https://github.com/nlpsandbox/nlpsandbox-schemas/blob/main/openapi/commons/components/schemas/TextLocationAnnotation.yaml
[TextPersonNameAnnotation]: https://github.com/nlpsandbox/nlpsandbox-schemas/blob/main/openapi/commons/components/schemas/TextPersonNameAnnotation.yaml
