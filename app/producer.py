from confluent_kafka import Producer, Consumer
import os, logging, sys, time, lorem

bootstrap_server = os.getenv('CONFLUENT_BOOTSTRAP_SERVER')
confluent_api_key = os.getenv('CONFLUENT_API_KEY')
confluent_secret_key = os.getenv('CONFLUENT_SECRET_KEY')
confluent_topic_name = os.getenv('CONFLUENT_TOPIC_NAME')

log = logging.getLogger()
log.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)

def delivery_report(err, msg):
    """Callback function to be called on delivery of message"""
    if err is not None:
        log.error('Message delivery failed: {}'.format(err))
    else:
        log.info('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def main():

    producer_conf = {
    'bootstrap.servers': bootstrap_server,
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': confluent_api_key,
    'sasl.password': confluent_secret_key,
}

    producer = Producer(producer_conf)
    log.info('Producer firing up!!')

    while True:
        message = lorem.sentence() 
        producer.produce(confluent_topic_name, value=message, callback=delivery_report)
        producer.flush()
        log.info('Produced message: {}'.format(message))
        time.sleep(1)

if __name__ == '__main__':
    main()
