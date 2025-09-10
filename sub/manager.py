from division_data import DivisionData
from publisher.get_paths import GetPaths
from speech_to_text.stt import STT
from logger.logger import Logger
import time

# <<< Creating instances >>>
division = DivisionData()
get_paths = GetPaths()
speech_to_text = STT()
logger = Logger.get_logger()

# <<< Variables >>>
directory_path = r"C:\Users\yba60\Desktop\podcasts"

# <<< Code flow >>>
list_paths = get_paths.absoluteFilePaths(directory_path)
count_paths = get_paths.get_count_path(list_paths)
all_data = division.get_list_data(count_paths)
time.sleep(10)
full_data = speech_to_text.add_for_all_the_metadata(all_data)
list_for_metadata, list_for_audio_path = division.get_metadata_parts(full_data)
print("-----")
print(list_for_metadata)
print("-----")
print(list_for_audio_path)