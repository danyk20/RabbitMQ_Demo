# RabbitMQ Example

## Prerequisites

- Running RabbitMQ
- Activated plugin
   ```shell
   rabbitmq-plugins enable rabbitmq_mqtt
   ```
- Opened ports in Firewall on RabbitMQ hosting machine
    ```shell
    firewall-cmd --permanent --add-port=1883/tcp
    firewall-cmd --permanent --add-port=5672/tcp
    firewall-cmd --permanent --add-port=15672/tcp
    systemctl restart firewalld
    firewall-cmd --list-all
    ```

## Instructions

1. Create `.env` file
   ```text
   BROKER_IP=<yours_broker_ip>
   ```
2. Install dependencies
    ```shell
    pipenv install
    ```
3. Consume a message—print all messages from the queue/topic
    ```shell
    pipenv run python3 consumer.py <protocol>
    ```
4. Publish a message—first string argument from command line will be sent to the broker
    ```shell
    pipenv run python3 producer.py <protocol> <your_message>
    ```