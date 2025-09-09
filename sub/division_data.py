from listener_to_topic import listen_kafka
from logger.logger import Logger
import time

class DivisionData:
    logger = Logger.get_logger()

    def get_list_data(self)->list:
        self.logger.info("listening...")

        consumer = listen_kafka()
        list_all_data = []
        try:
            for message in consumer:
                list_all_data.append(message.value)
                self.logger.info(message)

            consumer.close()
            return list_all_data
        except KeyboardInterrupt:
            self.logger.info("Listening stopped")

    
    def get_metadata_parts(self, all_data: list)->list:
        self.logger.info("enter")
        my_list = []
        for message in all_data:
            self.logger.info("enter")
            a = message.pop("Path", None)
            self.logger.info(a)
            my_list.append(message)
            self.logger.info(my_list)
            time.sleep(3)

        return my_list

            
