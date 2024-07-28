from utils.helpers import greet, save_memory_status, read_memory_status
from file_system import FileSystem
from memory import MemoryManager
from process_manager import ProcessManager
from system_info import SystemInfo
from files_log import FilesLog

class Core:
    def __init__(self, memory_size=1024):
        # Initialize components
        self.memory_manager = MemoryManager(size=memory_size)
        self.file_system = FileSystem()
        self.process_manager = ProcessManager()
        self.system_info = SystemInfo()
        self.files_log = FilesLog()
        self.is_recovering = False

    def greet_user(self, name):
        """Wywołuje funkcję powitania z helpera."""
        print(greet(name))

    def save_memory_status(self, file_path):
        """Zapisuje status pamięci do pliku JSON."""
        status = self.memory_manager.get_memory_status()
        save_memory_status(status, file_path)

    def read_memory_status(self, file_path):
        """Odczytuje status pamięci z pliku JSON."""
        return read_memory_status(file_path)

    def create_file(self, path, content=""):
        """Tworzy plik z danym contentem w określonym folderze."""
        self.file_system.create_file(path, content)

    def read_file(self, path):
        """Odczytuje zawartość pliku."""
        return self.file_system.read_file(path)

    def delete_file(self, path):
        """Usuwa plik."""
        self.file_system.delete_file(path)

    def create_directory(self, path):
        """Tworzy katalog (folder)."""
        try:
            self.file_system.create_directory(path)
        except FileExistsError as e:
            print(f"Error: {e}")

    def delete_directory(self, path):
        """Usuwa katalog (folder) i jego zawartość."""
        try:
            self.file_system.delete_directory(path)
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def list_files(self, path):
        """Wyświetla listę plików w katalogu."""
        try:
            files = self.file_system.list_files(path)
            print("Files in directory:", files)
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def allocate_memory(self, process_id, amount):
        """Przydziela pamięć dla procesu."""
        try:
            address = self.memory_manager.allocate(process_id, amount)
            print(f"Memory allocated at address {address}")
            self.files_log.allocate_memory_block(address, process_id)
        except MemoryError as e:
            self.error_crash_system("Memory allocation failed", str(e))

    def deallocate_memory(self, process_id):
        """Zwalnia pamięć dla procesu."""
        try:
            address = self.memory_manager.deallocate(process_id)
            print(f"Memory deallocated for process {process_id}")
            self.files_log.deallocate_memory_block(address)
        except ValueError as e:
            self.error_crash_system("Memory deallocation failed", str(e))

    def write_memory(self, address, data):
        """Zapisuje dane do pamięci."""
        try:
            self.memory_manager.write_memory(address, data)
            print("Data written to memory")
        except ValueError as e:
            self.error_crash_system("Memory write failed", str(e))

    def read_memory(self, address, length):
        """Odczytuje dane z pamięci."""
        try:
            data = self.memory_manager.read_memory(address, length)
            print(f"Data read from memory: {data}")
        except ValueError as e:
            self.error_crash_system("Memory read failed", str(e))

    def display_memory_status(self):
        """Wyświetla status pamięci."""
        status = self.memory_manager.get_memory_status()
        print("Memory Status:")
        print(f"Free blocks: {status['free_blocks']}")
        print(f"Occupied blocks: {status['occupied_blocks']}")

    def start_process(self, process_id, process_function, *args):
        """Uruchamia proces."""
        self.process_manager.start_process(process_id, process_function, *args)

    def stop_process(self, process_id):
        """Zatrzymuje proces."""
        self.process_manager.stop_process(process_id)

    def get_system_info(self):
        """Zwraca informacje o systemie."""
        return self.system_info.get_info()

    def compt(self):
        """Pokazuje dane o komputerze."""
        try:
            info = self.get_system_info()
            print("System Information:")
            for key, value in info.items():
                print(f"{key}: {value}")
        except Exception as e:
            print(f"Error retrieving system information: {e}")

    def error_crash_system(self, error_message, error_code):
        """Wyświetla komunikat o błędzie systemowym i włącza tryb odzyskiwania."""
        print("\nError Crash Of System")
        print(f"Error Code: {error_code}")
        print(f"Message: {error_message}\n")
        self.is_recovering = True
        self.enter_recovery_mode()

    def enter_recovery_mode(self):
        """Wchodzi w tryb odzyskiwania systemu."""
        if not self.is_recovering:
            return
        print("Entering Recovery Mode...")
        self.files_log.create_initial_blocks()  # Re-create missing files
        print("Recovery Mode: System is attempting to restore stability.")
        self.is_recovering = False  # Exit recovery mode after attempting restore

    def self_tsc(self):
        """Automatycznie wykonuje TSC."""
        print("Performing TSC...")
        self.error_crash_system("Tragic system crash", "0xTSC")

    def self_recoverysys(self):
        """Automatycznie wykonuje tryb odzyskiwania systemu."""
        print("Performing system recovery...")
        self.enter_recovery_mode()

# Testowanie funkcji core.py
if __name__ == "__main__":
    core = Core()

    # Testowanie funkcji greet_user
    core.greet_user("Alice")

    # Zapisz status pamięci do pliku
    core.save_memory_status("memory_status.json")

    # Odczytaj status pamięci z pliku
    status = core.read_memory_status("memory_status.json")
    print("Memory Status read from file:", status)

    # Testowanie funkcji zarządzania plikami
    core.create_directory("example_dir")
    core.create_file("example_dir/example_file.txt", "Hello, World!")
    print(core.read_file("example_dir/example_file.txt"))
    core.delete_file("example_dir/example_file.txt")
    core.delete_directory("example_dir")

    # Symulacja awarii systemu
    core.self_tsc()

    # Testowanie odzyskiwania systemu
    core.self_recoverysys()
