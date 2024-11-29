import sys
import os

from dotenv import load_dotenv

load_dotenv()


def publish(protocol: str, message: str) -> None:
    if protocol.upper() == "MQTT":
        publish_mqtt(message)
    elif protocol.upper() == "AMQP":
        publish_amqp(message)


def publish_amqp(message: str, routing_key: str = 'test', exchange: str = '', queue_name: str = 'test') -> None:
    import pika
    connection = pika.BlockingConnection(pika.ConnectionParameters(os.getenv('BROKER_IP')))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    channel.basic_publish(exchange=exchange,
                          routing_key=routing_key,
                          body=message)
    print("Message published!")

    connection.close()


def publish_mqtt(message: str, topic: str = 'test') -> None:
    client = connect_mqtt()
    client.loop_start()
    send(client, message, topic)
    client.loop_stop()


def connect_mqtt():
    import paho.mqtt.client as mqtt
    def on_connect(_client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'test')
    client.on_connect = on_connect
    client.connect(os.getenv('BROKER_IP'), int(os.getenv('MQTT_PORT')))
    return client


def send(client, message: str, topic: str = 'test'):
    while True:
        result = client.publish(topic, message)
        status = result[0]
        if status == 0:
            print(f"Send `{message}` to topic `{topic}`")
            break
        else:
            print(f"Failed to send message to topic {topic}")


publish(sys.argv[1], sys.argv[2])
