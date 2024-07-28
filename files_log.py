import os
import json
from datetime import datetime

class FilesLog:
    def __init__(self):
        self.data_dir = 'data'
        self.memory_dir = os.path.join(self.data_dir, 'memory')
        self.keys_dir = os.path.join(self.data_dir, 'keys')
        self.users_dir = os.path.join(self.data_dir, 'users')

        os.makedirs(self.memory_dir, exist_ok=True)
        os.makedirs(self.keys_dir, exist_ok=True)
        os.makedirs(self.users_dir, exist_ok=True)

    def create_memory_block(self, block_id, amount, process_id):
        """Tworzy blok pamięci w formacie JSON."""
        memory_block = {
            'block_id': block_id,
            'amount': amount,
            'process_id': process_id,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        file_path = os.path.join(self.memory_dir, f'memory_block_{block_id}.json')
        with open(file_path, 'w') as file:
            json.dump(memory_block, file)

    def delete_memory_block(self, block_id):
        """Usuwa blok pamięci w formacie JSON."""
        file_path = os.path.join(self.memory_dir, f'memory_block_{block_id}.json')
        if os.path.isfile(file_path):
            os.remove(file_path)

    def save_user(self, username, password):
        """Zapisuje użytkownika w formacie JSON."""
        user_data = {
            'username': username,
            'password': password,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        file_path = os.path.join(self.users_dir, f'{username}.json')
        with open(file_path, 'w') as file:
            json.dump(user_data, file)

    def get_user(self, username):
        """Odczytuje dane użytkownika z pliku JSON."""
        file_path = os.path.join(self.users_dir, f'{username}.json')
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return None

    def create_key_file(self, key_name, passkey):
        """Tworzy plik klucza w formacie JSON."""
        key_data = {
            'key_name': key_name,
            'passkey': passkey,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        file_path = os.path.join(self.keys_dir, f'{key_name}.json')
        with open(file_path, 'w') as file:
            json.dump(key_data, file)

    def delete_key_file(self, key_name):
        """Usuwa plik klucza w formacie JSON."""
        file_path = os.path.join(self.keys_dir, f'{key_name}.json')
        if os.path.isfile(file_path):
            os.remove(file_path)

    def save_memory_status(self, status):
        """Zapisuje status pamięci do pliku JSON."""
        file_path = os.path.join(self.memory_dir, 'memory_status.json')
        with open(file_path, 'w') as file:
            json.dump(status, file)

    def read_memory_status(self):
        """Odczytuje status pamięci z pliku JSON."""
        file_path = os.path.join(self.memory_dir, 'memory_status.json')
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return None

    def create_cpu_block(self, block_id, process_id):
        """Tworzy blok procesora w formacie JSON."""
        cpu_block = {
            'block_id': block_id,
            'process_id': process_id,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        file_path = os.path.join(self.memory_dir, f'cpu_block_{block_id}.json')
        with open(file_path, 'w') as file:
            json.dump(cpu_block, file)

    def delete_cpu_block(self, block_id):
        """Usuwa blok procesora w formacie JSON."""
        file_path = os.path.join(self.memory_dir, f'cpu_block_{block_id}.json')
        if os.path.isfile(file_path):
            os.remove(file_path)

    def create_ram_block(self, block_id, process_id):
        """Tworzy blok pamięci RAM w formacie JSON."""
        ram_block = {
            'block_id': block_id,
            'process_id': process_id,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        file_path = os.path.join(self.memory_dir, f'ram_block_{block_id}.json')
        with open(file_path, 'w') as file:
            json.dump(ram_block, file)

    def delete_ram_block(self, block_id):
        """Usuwa blok pamięci RAM w formacie JSON."""
        file_path = os.path.join(self.memory_dir, f'ram_block_{block_id}.json')
        if os.path.isfile(file_path):
            os.remove(file_path)
