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
print(list_metadata)