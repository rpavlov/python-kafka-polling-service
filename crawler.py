from dotenv import load_dotenv
import os
import requests
import logging
from kafka import KafkaProducer
import kafka.errors as Errors

logger = logging.getLogger()

log_format = logging.Formatter("%(asctime)-15s %(levelname)-2s %(message)s")
sh = logging.StreamHandler()
sh.setFormatter(log_format)

logger.addHandler(sh)
logger.setLevel(logging.ERROR)


def init_kafka_producer() -> KafkaProducer:
    try:
        producer = KafkaProducer(
            bootstrap_servers=os.getenv("KAFKA_URI"),
            security_protocol="SSL",
            ssl_cafile=os.getenv("KAFKA_PEM_FILE"),
            ssl_certfile=os.getenv("KAFKA_CERT_FILE"),
            ssl_keyfile=os.getenv("KAFKA_KEY_FILE"),
        )
    except (Errors.NoBrokersAvailable, Errors.BrokerResponseError) as e:
        logger.error(
            "Got %s error when attempting to connect to Kafka service. Is it running?",
            e,
        )
    return producer


def request(url: str) -> requests.Response:
    try:
        return requests.get("http://" + url, timeout=3)
    except requests.exceptions.ConnectionError as e:
        logger.error("Got %s error when attempting to connect to %s.", e, url)


def crawl(producer: KafkaProducer):
    try:
        with open("inventory.ini", "r") as hosts_file:
            for host in hosts_file:
                response = request(host.strip())
                if response:
                    response_seconds = response.elapsed.total_seconds()
                    message = f"Got {response} for {host.strip()} in {response_seconds} seconds."
                    producer.send(os.getenv("TOPIC_NAME"), message.encode("utf-8"))
                else:
                    logging.debug(
                        "Got non 20x response for %s. Got %s instead",
                        host.strip(),
                        response,
                    )
    except OSError as e:
        logger.error(
            "Got %s error when loading inventory.ini. Is it present and readable?", e
        )


if __name__ == "__main__":
    load_dotenv()
    producer = init_kafka_producer()
    if producer:
        crawl(producer)
