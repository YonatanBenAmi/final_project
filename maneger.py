from get_paths import GetPaths
from get_metadata import GetMetadata

class Maneger:
    # <<< Creating instances >>>
    get_paths = GetPaths()
    get_metadata = GetMetadata()

    # <<< Functions >>>
    def get_list_metadata(self, list_paths) -> list:
        list_metadata = []
        for path in list_paths:
            list_metadata.append(self.get_metadata.get_file_metadata(path))
        return list_metadata

        