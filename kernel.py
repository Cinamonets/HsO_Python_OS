import json
import os
from datetime import datetime
from files_log import FilesLog

class Kernel:
    def __init__(self):
        self.files_log = FilesLog()
        self.memory_size = 1024
        self.memory = [None] * self.memory_size
        self.version = "1.0.0"
        self.processes = {}
        self.tsc_count = 0
        self.recovery_mode = False

    def allocate_memory(self, process_id, amount):
        """Allocate memory for a process."""
        if amount <= 0 or amount > self.memory_size:
            self._trigger_tsc("Invalid memory amount for allocation.")
            return

        for i in range(self.memory_size):
            if self.memory[i] is None:
                if amount <= self.memory_size - i:
                    for j in range(i, i + amount):
                        self.memory[j] = process_id
                    self.files_log.create_memory_block(i, amount, process_id)
                    print(f"Memory allocated at address {i} for process {process_id}")
                    return
        self._trigger_tsc("Not enough memory to allocate.")

    def deallocate_memory(self, process_id):
        """Deallocate memory for a process."""
        for i in range(self.memory_size):
            if self.memory[i] == process_id:
                self.memory[i] = None
                self.files_log.remove_memory_block(i)
        print(f"Memory deallocated for process {process_id}")

    def write_memory(self, address, data):
        """Write data to memory."""
        if address < 0 or address >= self.memory_size:
            self._trigger_tsc("Invalid memory address for write.")
            return

        if not isinstance(data, list) or len(data) + address > self.memory_size:
            self._trigger_tsc("Invalid data for memory write.")
            return

        for i in range(len(data)):
            self.memory[address + i] = data[i]
        print("Data written to memory")

    def read_memory(self, address, length):
        """Read data from memory."""
        if address < 0 or address + length > self.memory_size:
            self._trigger_tsc("Invalid memory range for read.")
            return

        data = self.memory[address:address + length]
        print(f"Data read from memory: {data}")
        return data

    def display_memory_status(self):
        """Display memory status."""
        free_blocks = sum(1 for block in self.memory if block is None)
        occupied_blocks = self.memory_size - free_blocks
        print("Memory Status:")
        print(f"Free blocks: {free_blocks}")
        print(f"Occupied blocks: {occupied_blocks}")

    def update_kernel(self, new_version):
        """Update kernel version."""
        self.version = new_version
        print(f"Kernel version updated to {new_version}")

    def _trigger_tsc(self, error_message):
        """Trigger a tragic system crash (TSC)."""
        self.tsc_count += 1
        print("\nTSC (Tragic System Crash)")
        print(f"Error Message: {error_message}")
        print(f"Error Code: TSC-{self.tsc_count}")
        if self.tsc_count >= 3:
            self.enter_recovery_mode()
        else:
            self.reboot_system()

    def reboot_system(self):
        """Reboot the system."""
        print("System rebooting...")
        # Here you would add actual reboot logic if needed

    def enter_recovery_mode(self):
        """Enter recovery mode."""
        if not self.recovery_mode:
            self.recovery_mode = True
            print("Entering Recovery Mode...")
            self.scan_and_repair()
            self.reboot_system()

    def scan_and_repair(self):
        """Scan for missing files and attempt repair."""
        print("Scanning for missing files and attempting repair...")
        missing_files = self.files_log.check_for_missing_files()
        if missing_files:
            for file in missing_files:
                self.files_log.recover_file(file)
            print("Files recovered.")

    def self_tsc(self):
        """Manually trigger a TSC."""
        self._trigger_tsc("Manual TSC triggered.")

    def self_recoverysys(self):
        """Manually enter recovery mode."""
        self.enter_recovery_mode()

    def get_system_info(self):
        """Get system information."""
        info = {
            "version": self.version,
            "memory_size": self.memory_size,
            "processes": self.processes
        }
        return info

if __name__ == "__main__":
    kernel = Kernel()
    kernel.display_memory_status()
    kernel.allocate_memory(1, 10)
    kernel.write_memory(0, [1, 2, 3, 4, 5])
    kernel.read_memory(0, 5)
    kernel.deallocate_memory(1)
    kernel.update_kernel("2.0.0")
    kernel.self_tsc()
    kernel.self_recoverysys()
