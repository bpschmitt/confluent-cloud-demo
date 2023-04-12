# Producer / Consumer Demo Apps

Local testing instructions.

```
export CONFLUENT_BOOTSTRAP_SERVER = <your bootstrap server>
export CONFLUENT_API_KEY = <your api key>
export CONFLUENT_SECRET_KEY = <your secret key>
export CONFLUENT_TOPIC_NAME = <topic name>

python3 producer.py
python3 consumer.py
```