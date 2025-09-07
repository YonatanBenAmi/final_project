from kafka import KafkaConsumer
import json

def listen_kafka():
    consumer = KafkaConsumer(
        "metadata",  # The topic name
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',  # שיקרא מהתחלה אם לא קראנו עדיין
        enable_auto_commit=True,
        group_id="full metadata",
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    print("listening")
    try:
        for message in consumer:
            print(f"[{message.topic}] {message.value}")
    except KeyboardInterrupt:
        print("stopt thre lesenir ")


listen_kafka()