import os

class GetPaths:

    directory_path = r"C:\Users\yba60\Desktop\podcasts"

    # Return list of all faths files in this directory(directory_path)
    def absoluteFilePaths(self):
        path_files = []
        for root, dirs, files in os.walk(os.path.abspath(self.directory_path)):
            for file in files:
                path_files.append(os.path.join(root, file))
        return path_files
