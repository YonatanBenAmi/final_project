from maneger import Maneger
from get_paths import GetPaths
from get_metadata import GetMetadata
from send_to_kafka import SendToKafka

# <<< Creating instances >>>
maneger = Maneger()
get_paths = GetPaths()
get_metadata = GetMetadata()
send_to_kafka = SendToKafka()


directory_path = r"C:\Users\yba60\Desktop\podcasts"

list_paths = get_paths.absoluteFilePaths(directory_path) # List of all paths.
list_metadata = maneger.get_list_metadata(list_paths) # List of all metadata.
maneger.send_all_metadata_to_kafka(list_paths, list_metadata) # Send to kafka all full metadata.