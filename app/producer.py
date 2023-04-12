from confluent_kafka import Producer, Consumer
import time, os
import lorem

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
    producer_conf = {
    'bootstrap.servers': bootstrap_server,
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': confluent_api_key,
    'sasl.password': confluent_secret_key,
}

    producer = Producer(producer_conf)
    print('Producer firing up!!')

    while True:
        message = lorem.sentence() 
        producer.produce('demo', value=message, callback=delivery_report)
        producer.flush()
        print('Produced message: {}'.format(message))
        time.sleep(1)

if __name__ == '__main__':
    main()
