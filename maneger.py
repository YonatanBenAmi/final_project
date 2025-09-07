from get_paths import GetPaths

get_paths = GetPaths()

list_paths = get_paths.absoluteFilePaths()

for path in list_paths:
    print(path)