
# TODO: You need to implement the consumption logic and connection to RabbitMQ here.
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        "localhost", credentials=pika.PlainCredentials("guest", "guest")
    )
)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

channel.queue_declare(queue='hello-consumer-1')

channel.queue_bind(exchange='logs', queue='hello-consumer-1')

def log_to_file(log_entry: str):
    with open('./log.log', 'a+') as log_file:
        log_file.write(log_entry + '\n')
        log_file.flush()

def callback(ch, method, properties, body):
    log_entry = body.decode('utf-8')
    # print(f" [x] Received log: {log_entry}")
    log_to_file(log_entry)


print('Waiting for logs....')
# TODO: consume logs here
channel.basic_consume(
    queue="hello-consumer-1", auto_ack=True, on_message_callback=callback
)
channel.start_consuming()

