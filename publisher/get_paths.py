import os

class GetPaths:

    # Return list of all faths files in this directory(directory_path)
    def absoluteFilePaths(self, directory_path)->list:
        path_files = []
        for root, dirs, files in os.walk(os.path.abspath(directory_path)):
            for file in files:
                path_files.append(os.path.join(root, file))
        return path_files

    def get_count_path(self, list_paths):
        return len(list_paths)
