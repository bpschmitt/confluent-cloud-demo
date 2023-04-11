from confluent_kafka import Consumer, KafkaError
import time
import os

bootstrap_server = os.getenv('CONFLUENT_BOOTSTRAP_SERVER')
confluent_api_key = os.getenv('CONFLUENT_API_KEY')
confluent_secret_key = os.getenv('CONFLUENT_SECRET_KEY')

def delivery_report(err, msg):
    """Callback function to be called on delivery of message"""
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def main():
    consumer_conf = {
    'bootstrap.servers': bootstrap_server,
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': confluent_api_key,
    'sasl.password': confluent_secret_key,
    'group.id': 'demo'
}

    consumer = Consumer(consumer_conf)

   # Example of consuming messages from a topic
    consumer.subscribe(['demo'])

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('End of partition event detected')
            else:
                print('Error while consuming messages: {}'.format(msg.error()))
        else:
            print('Received message: key={}, value={}, partition={}, offset={}'.format(
                msg.key(), msg.value(), msg.partition(), msg.offset()))
        
if __name__ == '__main__':
    main()
