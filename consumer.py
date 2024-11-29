import os
import sys

from dotenv import load_dotenv

load_dotenv()


def process_amqp_message(queue_name: str = 'test') -> None:
    import pika
    connection = pika.BlockingConnection(pika.ConnectionParameters(os.getenv('BROKER_IP')))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue=queue_name,
                          auto_ack=True,
                          on_message_callback=callback)
    channel.start_consuming()


def process_mqtt_message(topic_name: str = 'test') -> None:
    import paho.mqtt.client as mqtt  # Replace 'your_topic_name' with the appropriate topic

    def on_message(client, userdata, msg):
        print(f" [x] Received {msg.payload.decode()}")

    client = mqtt.Client()
    client.connect(os.getenv('BROKER_IP'))
    client.on_message = on_message

    client.subscribe(topic_name)
    client.loop_forever()


try:
    if sys.argv[1] == 'amqp':
        process_amqp_message()
    elif sys.argv[1] == 'mqtt':
        process_mqtt_message()
except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
