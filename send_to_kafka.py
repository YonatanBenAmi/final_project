from kafka import KafkaProducer
import json

class SendToKafka:

    def send(self, json):
        producer = self.get_producer()
        self.publish_message(producer, "metadata", json)
        print("200: OK")
                    
      
    def get_producer(self):
            return KafkaProducer(
                bootstrap_servers=['localhost:9092'],
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )

    def publish_message(self, producer, topic, message):
        producer.send(topic, message)
        producer.flush()

    