from get_paths import GetPaths
from get_metadata import GetMetadata
from send_to_kafka import SendToKafka
import time
import json

class Maneger:
    # <<< Creating instances >>>
    get_paths = GetPaths()
    get_metadata = GetMetadata()
    send_to_kafka = SendToKafka()

    # <<< Functions >>>

    # Get list of paths and return list of metadata.
    def get_list_metadata(self, list_paths) -> list:
        list_metadata = []
        for path in list_paths:
            list_metadata.append(self.get_metadata.get_file_metadata(path))
        return list_metadata
    
    # Get path and metadata, Return full metadata(metadata + path).
    def get_full_metadata(self, path:str, metadata:dict)->dict:
        metadata["Path"] = path
        return metadata

    # Send all full metadata(metadata + path) to kafka.
    def send_all_metadata_to_kafka(self, list_paths, list_metadata):
        for i in range(len(list_paths)):
            full_metadata = self.get_full_metadata(list_paths[i], list_metadata[i])
            self.send_to_kafka.send(full_metadata)
            time.sleep(1)
            

