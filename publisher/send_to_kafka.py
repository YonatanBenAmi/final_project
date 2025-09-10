from kafka import KafkaProducer
import json
from logger.logger import Logger

class SendToKafka:
    # <<< Creating instances >>>
    logger = Logger.get_logger()

    # <<< Functions >>>
    # Send dict to Kafka.
    def send(self, message):
        producer = self.get_producer()
        self.publish_message(producer, "metadata", message)
        self.logger.info("OK - Sent to Kafka successfully.")

    # Get the producer.
    def get_producer(self):
            return KafkaProducer(
                bootstrap_servers=['localhost:9092'],
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )

    # Publish the dict(message)
    def publish_message(self, producer, topic, message):
        producer.send(topic, message)
        producer.flush()

    