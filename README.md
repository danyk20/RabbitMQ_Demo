# Instructions

1. Create `.env` file
   ```text
   BROKER_IP=<yours_broker_ip>
   ```
2. Install dependencies
    ```shell
    pipenv install
    ```
3. Publish a message—first string argument from command line will be sent to the broker
    ```shell
    pipenv run python3 producer.py <your_message>
    ```
4. Consume a message—print all messages from the queue
    ```shell
    pipenv run python3 consumer.py
    ```