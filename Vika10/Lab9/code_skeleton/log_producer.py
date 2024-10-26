#!/usr/bin/env python
import string
import time
import random

# TODO: RabbitMQ connection logic goes here
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        "localhost", credentials=pika.PlainCredentials("guest", "guest")
    )
)
channel = connection.channel()

def random_log() -> str:
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))


try:
    while True:
        log_entry = random_log()
        print(f'Publishing log: {log_entry}')
        # TODO: publish logs
        channel.basic_publish(exchange='logs', routing_key='', body=log_entry)
        time.sleep(3)
finally:
    connection.close()

