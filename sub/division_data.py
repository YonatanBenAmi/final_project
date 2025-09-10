from listener_to_topic import listen_kafka
from logger.logger import Logger
import time

class DivisionData:
    # <<< Creating instances >>>
    logger = Logger.get_logger()

    # <<< Functions >>>

    def get_list_data(self, count_paths)->list:
        self.logger.info("listening...")
        consumer = listen_kafka()
        list_all_data = []

        try:
            for message in consumer:
                count_paths -= 1
                list_all_data.append(message.value)
                self.logger.info(message.value)
                if count_paths <= 0:
                    break
            consumer.close()
            return list_all_data
        except KeyboardInterrupt:
            self.logger.info("Listening stopped")

    
    def get_metadata_parts(self, all_data: list)->tuple:
        list_for_metadata = []
        list_for_audio_paths = []
        for message in all_data:
            list_for_audio_paths.append(message["Path"])
            list_for_audio_paths.append(message["File name"])
            message.pop("Path", None)
            list_for_metadata.append(message)
            self.logger.info(message)

        return list_for_metadata, list_for_audio_paths

            
