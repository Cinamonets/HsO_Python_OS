import os
import json
import platform
import datetime
from files_log import FilesLog
from kernel import Kernel

class Shell:
    def __init__(self, kernel):
        self.kernel = kernel
        self.files_log = FilesLog()

    def start(self):
        self.login()
        print("Welcome to the simulated OS!")
        while True:
            command = input(">> ").strip().split()
            if not command:
                continue

            cmd = command[0]
            args = command[1:]

            if cmd == "exit":
                break
            elif cmd == "allocate":
                self.allocate_memory(args)
            elif cmd == "deallocate":
                self.deallocate_memory(args)
            elif cmd == "write":
                self.write_memory(args)
            elif cmd == "read":
                self.read_memory(args)
            elif cmd == "mem":
                self.kernel.display_memory_status()
            elif cmd == "ver":
                print(f"Simulated OS Version: {self.kernel.version}")
            elif cmd == "compt":
                self.display_computer_info()
            elif cmd == "help":
                self.display_help()
            elif cmd == "settings":
                self.change_settings()
            elif cmd == "update_kernel":
                self.update_kernel(args)
            elif cmd == "time":
                self.display_time()
            elif cmd == "date":
                self.display_date()
            elif cmd == "snakeexit (NOT SNAKE GAME)":
                self.run_snake_game()
            else:
                print("Unknown command")

    def allocate_memory(self, args):
        if len(args) < 2:
            print("Usage: allocate <process_id> <amount>")
        else:
            try:
                process_id = int(args[0])
                amount = int(args[1])
                self.kernel.allocate_memory(process_id, amount)
            except ValueError:
                print("Invalid input for process_id or amount")

    def deallocate_memory(self, args):
        if len(args) < 1:
            print("Usage: deallocate <process_id>")
        else:
            try:
                process_id = int(args[0])
                self.kernel.deallocate_memory(process_id)
            except ValueError:
                print("Invalid process_id")

    def write_memory(self, args):
        if len(args) < 2:
            print("Usage: write <address> <data>")
        else:
            try:
                address = int(args[0])
                data = list(map(int, args[1:]))
                self.kernel.write_memory(address, data)
            except ValueError:
                print("Invalid address or data")

    def read_memory(self, args):
        if len(args) < 2:
            print("Usage: read <address> <length>")
        else:
            try:
                address = int(args[0])
                length = int(args[1])
                self.kernel.read_memory(address, length)
            except ValueError:
                print("Invalid address or length")

    def display_computer_info(self):
        print("Computer Information:")
        print(f"System: {platform.system()}")
        print(f"Node Name: {platform.node()}")
        print(f"Release: {platform.release()}")
        print(f"Version: {platform.version()}")
        print(f"Machine: {platform.machine()}")
        print(f"Processor: {platform.processor()}")

    def display_help(self):
        print("Available Commands:")
        print("allocate <process_id> <amount> - Allocate memory for a process")
        print("deallocate <process_id> - Deallocate memory for a process")
        print("write <address> <data> - Write data to memory")
        print("read <address> <length> - Read data from memory")
        print("mem - Display memory status")
        print("ver - Display OS version")
        print("compt - Display computer information")
        print("help - Display this help message")
        print("settings - Change settings")
        print("update_kernel <new_version> - Update the kernel version")
        print("time - Display current time")
        print("date - Display current date")
        print("snake - Play the Snake game")
        print("exit - Exit the shell")

    def change_settings(self):
        print("Settings Menu:")
        new_version = input("Enter new version: ").strip()
        if new_version:
            self.kernel.version = new_version
            print(f"Version updated to: {self.kernel.version}")

    def update_kernel(self, args):
        if len(args) < 1:
            print("Usage: update_kernel <new_version>")
        else:
            new_version = args[0]
            self.kernel.update_kernel(new_version)

    def display_time(self):
        print(f"Current time: {datetime.datetime.now().strftime('%H:%M:%S')}")

    def display_date(self):
        print(f"Current date: {datetime.datetime.now().strftime('%Y-%m-%d')}")

    def run_snake_game(self):
        import snake_game
        snake_game.run()

    def login(self):
        while True:
            username = input("Username: ").strip()
            user_data = self.files_log.get_user(username)
            if user_data is None:
                print("User not found. Creating new user.")
                password = input("Create a password: ").strip()
                self.files_log.save_user(username, password)
                print("User created successfully. Please log in.")
                continue
            
            password = input("Password: ").strip()
            if user_data['password'] == password:
                print(f"Welcome, {username}!")
                break
            else:
                print("Incorrect Password. Please try again.")

if __name__ == "__main__":
    kernel = Kernel()
    shell = Shell(kernel)
    shell.start()
