from get_paths import GetPaths

class Maneger:

    get_paths = GetPaths()

    def print_all_path_files(self):
        list_paths = self.get_paths.absoluteFilePaths()

        for path in list_paths:
            print(path)