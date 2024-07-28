import json
import os
from datetime import datetime

class MemoryBlock:
    def __init__(self, block_id, size):
        self.block_id = block_id
        self.size = size
        self.allocated = False
        self.process_id = None
        self.timestamp = None

    def allocate(self, process_id):
        self.allocated = True
        self.process_id = process_id
        self.timestamp = datetime.now().isoformat()

    def deallocate(self):
        self.allocated = False
        self.process_id = None
        self.timestamp = None

    def to_dict(self):
        return {
            'block_id': self.block_id,
            'size': self.size,
            'allocated': self.allocated,
            'process_id': self.process_id,
            'timestamp': self.timestamp
        }

class MemoryManager:
    def __init__(self, size=1024, block_size=1):
        self.total_size = size
        self.block_size = block_size
        self.blocks = [MemoryBlock(i, block_size) for i in range(size // block_size)]
        self.memory_dir = "data/memory"
        if not os.path.exists(self.memory_dir):
            os.makedirs(self.memory_dir)

    def allocate(self, process_id, amount):
        required_blocks = amount // self.block_size
        if amount % self.block_size != 0:
            required_blocks += 1

        free_blocks = [block for block in self.blocks if not block.allocated]
        if len(free_blocks) < required_blocks:
            raise MemoryError("Not enough memory available")

        allocated_blocks = free_blocks[:required_blocks]
        for block in allocated_blocks:
            block.allocate(process_id)
            self.save_block(block)

        return [block.block_id for block in allocated_blocks]

    def deallocate(self, process_id):
        for block in self.blocks:
            if block.allocated and block.process_id == process_id:
                block.deallocate()
                self.delete_block(block.block_id)

    def write_memory(self, address, data):
        if address < 0 or address >= len(self.blocks):
            raise ValueError("Invalid address")
        block = self.blocks[address]
        if not block.allocated:
            raise ValueError("Memory block is not allocated")
        block.data = data
        self.save_block(block)

    def read_memory(self, address, length):
        if address < 0 or address + length > len(self.blocks):
            raise ValueError("Invalid address or length")
        data = []
        for i in range(address, address + length):
            block = self.blocks[i]
            if not block.allocated:
                raise ValueError(f"Memory block at address {i} is not allocated")
            data.append(block.data)
        return data

    def get_memory_status(self):
        free_blocks = [block for block in self.blocks if not block.allocated]
        occupied_blocks = [block for block in self.blocks if block.allocated]
        return {
            'total_blocks': len(self.blocks),
            'free_blocks': len(free_blocks),
            'occupied_blocks': len(occupied_blocks)
        }

    def save_block(self, block):
        block_file = os.path.join(self.memory_dir, f"memory_block_{block.block_id}.json")
        with open(block_file, 'w') as f:
            json.dump(block.to_dict(), f)

    def delete_block(self, block_id):
        block_file = os.path.join(self.memory_dir, f"memory_block_{block_id}.json")
        if os.path.exists(block_file):
            os.remove(block_file)

# Testowanie funkcji w memory.py
if __name__ == "__main__":
    mm = MemoryManager(size=1024, block_size=1)

    # Alokowanie pamięci dla procesu
    process_id = 1
    amount = 10
    try:
        allocated_blocks = mm.allocate(process_id, amount)
        print(f"Memory allocated at blocks: {allocated_blocks}")
    except MemoryError as e:
        print(f"Memory allocation failed: {e}")

    # Wyświetlenie statusu pamięci
    status = mm.get_memory_status()
    print("Memory Status:")
    print(f"Total blocks: {status['total_blocks']}")
    print(f"Free blocks: {status['free_blocks']}")
    print(f"Occupied blocks: {status['occupied_blocks']}")

    # Zwalnianie pamięci dla procesu
    mm.deallocate(process_id)
    print(f"Memory deallocated for process {process_id}")

    # Wyświetlenie statusu pamięci po zwolnieniu
    status = mm.get_memory_status()
    print("Memory Status after deallocation:")
    print(f"Total blocks: {status['total_blocks']}")
    print(f"Free blocks: {status['free_blocks']}")
    print(f"Occupied blocks: {status['occupied_blocks']}")
