from maneger import Maneger
from get_paths import GetPaths
from get_metadata import GetMetadata

# <<< Creating instances >>>
maneger = Maneger()
get_paths = GetPaths()
get_metadata = GetMetadata()


directory_path = r"C:\Users\yba60\Desktop\podcasts"

list_paths = get_paths.absoluteFilePaths(directory_path)
list_metadata = maneger.get_list_metadata(list_paths)
json_metadata = maneger.get_data_in_json(list_paths[3], list_metadata[3])
print(json_metadata)