import random
import sys
from confluent_kafka import Producer
import socket

conf = {"bootstrap.servers": "localhost:9092", "client.id": socket.gethostname()}

producer = Producer(conf)

first_argument = sys.argv[1]
random_number = random.randint(0, 1000)
producer.produce(
    "hello-world", key=first_argument, value=f"hello world! - {random_number}"
)

producer.flush()
