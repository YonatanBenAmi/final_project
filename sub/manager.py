from division_data import DivisionData
from publisher.get_paths import GetPaths
import time


division = DivisionData()
get_paths = GetPaths()

directory_path = r"C:\Users\yba60\Desktop\podcasts"

list_paths = get_paths.absoluteFilePaths(directory_path)
count_paths = get_paths.get_count_path(list_paths)

all_data = division.get_list_data(count_paths)
time.sleep(10)
print("------------------------------------------")
list_for_metadata, list_for_audio_path = division.get_metadata_parts(all_data)
print(list_for_metadata)
print("-------------------------------")
print(list_for_audio_path)