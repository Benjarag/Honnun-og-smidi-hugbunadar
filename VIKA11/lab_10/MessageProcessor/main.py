import pika
from retry import retry


@retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
def get_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            "localhost", credentials=pika.PlainCredentials("guest", "guest")
        )
    )
    return connection
    # TODO: create rabbitmq connection
    
def callback(ch, method, properties, body):
    message = body.decode()
    print(f"Received message: {message}")  # Print the received message
    
    # Write the message to a text file
    with open('messages.txt', 'a') as f:
        f.write(message + '\n')  # Append the message to the file

if __name__ == '__main__':
    # TODO: consume message events and print them to console
    connection = get_connection()
    channel = connection.channel()

    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    channel.queue_declare(queue='queue')

    channel.queue_bind(exchange='logs', queue='queue')

    print('Waiting for logs....')
    # TODO: consume logs here
    channel.basic_consume(
        queue="queue", auto_ack=True, on_message_callback=callback
    )
    channel.start_consuming()


