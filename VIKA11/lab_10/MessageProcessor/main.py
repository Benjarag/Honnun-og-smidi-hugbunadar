import pika
from retry import retry

@retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
def get_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='rabbitmq',  
            credentials=pika.PlainCredentials('guest', 'guest')
        )
    )
    return connection

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")

if __name__ == '__main__':
    connection = get_connection()
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    result = channel.queue_declare('', exclusive=True)  # Generate a unique queue name
    queue_name = result.method.queue
    channel.queue_bind(exchange='logs', queue=queue_name)
    print('Waiting for messages. To exit press CTRL+C')
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Stopping the consumer...")
    finally:
        channel.stop_consuming()
        connection.close()
