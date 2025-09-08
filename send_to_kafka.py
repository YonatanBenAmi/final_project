from kafka import KafkaProducer
import json
from logger import Logger

class SendToKafka:

    logger = Logger.get_logger()

    def send(self, json):
        producer = self.get_producer()
        self.publish_message(producer, "metadata", json)
        self.logger.info("200: OK")
                    
      
    def get_producer(self):
            return KafkaProducer(
                bootstrap_servers=['localhost:9092'],
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )

    def publish_message(self, producer, topic, message):
        producer.send(topic, message)
        producer.flush()

    