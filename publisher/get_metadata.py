import os
import datetime

class GetMetadata:

    # Get file path and return metadata fields.
    def get_file_metadata(self, file_path):

        try:
            # <<< Variables >>>
            stats = os.stat(file_path) #Get stat_result object

            file_name = os.path.basename(file_path)
            file_size = stats.st_size  # Size in bytes
            creation_time = datetime.datetime.fromtimestamp(stats.st_ctime) # Creation time
            device = stats.st_dev # Device identifier

            metadata = {
            "File name": file_name,
            "File Size (bytes)": file_size,
            "Creation Time": creation_time.isoformat(),
            "Device Identifier": device
            }

            return metadata
        
        except FileNotFoundError:
            return "Error: File not found."
        except Exception as e:
            return f"An error occurred: {e}"