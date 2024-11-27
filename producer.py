import sys
import pika
import os
from dotenv import load_dotenv

load_dotenv()


def publish(message: str, routing_key: str = 'test', exchange: str = '', queue_name: str = 'test') -> None:
    connection = pika.BlockingConnection(pika.ConnectionParameters(os.getenv('BROKER_IP')))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    channel.basic_publish(exchange=exchange,
                          routing_key=routing_key,
                          body=message)
    print("Message published!")

    connection.close()

publish(sys.argv[1])