from confluent_kafka import Consumer, KafkaError
import os, logging, sys

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
    log.info('Consumer firing up!!')

   # Example of consuming messages from a topic
    consumer.subscribe([confluent_topic_name])

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                log.info('End of partition event detected')
            else:
                log.error('Error while consuming messages: {}'.format(msg.error()))
        else:
            log.info('Received message: key={}, value={}, partition={}, offset={}'.format(
                msg.key(), msg.value(), msg.partition(), msg.offset()))
        
if __name__ == '__main__':
    main()
