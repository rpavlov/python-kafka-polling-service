# Intro

The purpose of this tool is to crawl a given list of host URLS, store response data and then publish to an Apache Kafka topic. Successful requests will be published, while timeouts and failures will be logged. 

# Requirements
- Python 3.x

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

Add the list of urls to crawl in the `inventory.ini` file then invoke it with a regex string argument 

```bash
python crawler/crawler.py "\d+"
``` 

To see the messages being sent you can run the consumer in another terminal tab 

```bash
python consumer/consumer.py
```

as well as keeping an eye on the logfile

```bash
tail -f crawler.log
``` 
# Development

This project is setup to use a couple of python linters (Black and Flake8) via the [pre-commit](https://pre-commit.com/) package. In order to enable it after installing from requirements.txt please run `pre-commit install`.

# Testing

```bash
pytest tests
```

Testing is tricky because it relies on having the broker running, as well as having endpoints to hit. Ideally I would spend a few more hours to write mock servers and clients, but my time is limited :(  
There are a bunch more scenarios that I could write test cases for, such as missing/incorrect credentials, malformed urls, broker unresponsiveness, broker dies after successful connection, but I suppose we could discuss these later.

# TODO

- [x] pylint
- [x] docstrings
- [x] bootstrap a consumer for testing
- [x] Log to stdout as well. logfile is too noisy.

