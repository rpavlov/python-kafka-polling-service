# SRE Technical Challenge

The purpose of this tool is to crawl a given list of host URLS, store response data and then publish to an Apache Kafka topic.

# Requirements
- Python3.x

# Quickstart

1. Create a virtual env for package isolation.

```bash
python -m venv venv
```

2. And activate it.
```bash
source venv/bin/activate
```

3. Before installing the packages for this tool.
```bash
pip install -r requirements.txt
```

4. From the aiven console, download your Apache Kafka service's `service.cert`, `service.key` and `ca.pem` and place them in this project directory. Also take note of your service URI.
5. Finally, rename .env.example to .env and populate the variables with your own values.

# Usage

Add the list of urls or ips to crawl in the `inventory.ini` file.

# Development
This project is setup to use a couple of python linters (Black and Flake8) via the [pre-commit](https://pre-commit.com/) package. In order to enable it after installing from requirements.txt please run `pre-commit install`.

# Testing

# TODO

- [ ] pylint

# Notes


