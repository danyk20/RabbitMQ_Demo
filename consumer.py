import os
import sys
import pika
from dotenv import load_dotenv

load_dotenv()


def process_message(queue_name: str = 'test') -> None:
    connection = pika.BlockingConnection(pika.ConnectionParameters(os.getenv('BROKER_IP')))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue=queue_name,
                          auto_ack=True,
                          on_message_callback=callback)
    channel.start_consuming()


try:
    process_message()
except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
