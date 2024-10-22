from confluent_kafka import Consumer

conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "consumer-2-vol2",
    "auto.offset.reset": "smallest",
}

consumer = Consumer(conf)

consumer.subscribe(["hello-world"])
try:
    while True:

        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue

        print(
            f"Consumed message: {msg.key().decode('utf-8')}: {msg.value().decode('utf-8')}"
        )
finally:
    consumer.close()
