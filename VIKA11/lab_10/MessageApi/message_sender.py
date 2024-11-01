import pika
from retry import retry


class MessageSender:
    def __init__(self) -> None:
        # TODO: initiate connection
        self.connection = self.__get_connection()  # Create connection
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='logs', exchange_type='fanout')


    def send_message(self, message):
        # TODO: send message via rabbitmq
        self.channel.basic_publish(exchange='logs', routing_key='', body=message)

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        # TODO: create rabbitmq connection
        connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            "rabbitmq", credentials=pika.PlainCredentials("guest", "guest")
            )
        )
        return connection