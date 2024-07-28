class FileSystem:
    def __init__(self):
        # Korzeń naszego systemu plików
        self.files = {}
        self.directories = {'/': {}}
    
    def _get_node(self, path):
        """Helper function to get the node at the given path."""
        nodes = path.strip('/').split('/')
        current_node = self.directories
        
        for node in nodes:
            if node not in current_node:
                return None
            current_node = current_node[node]
        
        return current_node
    
    def _split_path(self, path, is_directory=False):
        """Helper function to split path into directory and file name."""
        nodes = path.strip('/').split('/')
        if is_directory:
            return '/'.join(nodes[:-1]), nodes[-1]
        else:
            return '/'.join(nodes[:-1]), nodes[-1]

    def create_file(self, path, content=""):
        """Tworzy plik z danym contentem w określonym folderze."""
        folder_path, file_name = self._split_path(path)
        if folder_path not in self.directories:
            raise FileNotFoundError(f"Directory '{folder_path}' not found.")
        
        # Zapisywanie zawartości pliku
        full_path = folder_path + '/' + file_name
        self.files[full_path] = content
        print(f"File created: {full_path}")

    def read_file(self, path):
        """Odczytuje zawartość pliku."""
        if path not in self.files:
            raise FileNotFoundError(f"No such file: {path}")
        return self.files[path]

    def delete_file(self, path):
        """Usuwa plik."""
        if path not in self.files:
            raise FileNotFoundError(f"No such file: {path}")
        del self.files[path]
        print(f"File deleted: {path}")

    def create_directory(self, path):
        """Tworzy katalog (folder)."""
        nodes = path.strip('/').split('/')
        current_node = self.directories
        full_path = '/'
        
        for node in nodes:
            if node not in current_node:
                current_node[node] = {}
            current_node = current_node[node]
            full_path = f"{full_path}/{node}".strip('/')
        
        if full_path in self.directories:
            raise FileExistsError(f"Directory '{full_path}' already exists.")
        
        self.directories[full_path] = {}
        print(f"Directory created: {full_path}")

    def delete_directory(self, path):
        """Usuwa katalog (folder) i jego zawartość."""
        if path not in self.directories:
            raise FileNotFoundError(f"No such directory: {path}")

        # Usuwanie wszystkich plików w katalogu
        to_delete = []
        for file in self.files:
            if file.startswith(path + '/'):
                to_delete.append(file)
        
        for file in to_delete:
            self.delete_file(file)

        # Usuwanie katalogu
        parent_path, dir_name = self._split_path(path, True)
        parent_node = self._get_node(parent_path)
        if parent_node and dir_name in parent_node:
            del parent_node[dir_name]
            print(f"Directory deleted: {path}")

    def list_files(self, path):
        """Wyświetla listę plików w katalogu."""
        if path not in self.directories:
            raise FileNotFoundError(f"No such directory: {path}")

        files = [file for file in self.files if file.startswith(path + '/')]
        return files
