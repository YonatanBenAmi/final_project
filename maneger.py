from get_paths import GetPaths
from get_metadata import GetMetadata
import json

class Maneger:
    # <<< Creating instances >>>
    get_paths = GetPaths()
    get_metadata = GetMetadata()

    # <<< Functions >>>
    # Get list of paths and return list of metadata
    def get_list_metadata(self, list_paths) -> list:
        list_metadata = []
        for path in list_paths:
            list_metadata.append(self.get_metadata.get_file_metadata(path))
        return list_metadata
    
    # Get path and metadata, Return json file(metadata + path)
    def get_data_in_json(self, path, metadata):
        metadata["Path"] = path
        json_metadata = "metadata.json"
        with open(json_metadata, "w") as json_file:
            json.dump(metadata, json_file, indent=4)
            return json_file

        