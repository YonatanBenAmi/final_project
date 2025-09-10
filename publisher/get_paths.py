import os

class GetPaths:
    # <<< Functions >>>
    # Get directory path, Return list of all paths files in this directory(directory_path)
    def absoluteFilePaths(self, directory_path)->list:
        path_files = []
        for root, dirs, files in os.walk(os.path.abspath(directory_path)):
            for file in files:
                path_files.append(os.path.join(root, file))
        return path_files


    # Get list of paths and return the length list.
    def get_count_path(self, list_paths):
        return len(list_paths)
