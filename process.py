class Process:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.state = "ready"

    def __str__(self):
        return f"Process(pid={self.pid}, name={self.name}, state={self.state})"

class ProcessManager:
    def __init__(self):
        self.processes = {}
        self.next_pid = 1

    def create_process(self, name):
        pid = self.next_pid
        self.next_pid += 1
        process = Process(pid, name)
        self.processes[pid] = process
        return process

    def list_processes(self):
        for process in self.processes.values():
            print(process)

    def stop_process(self, pid):
        if pid in self.processes:
            self.processes[pid].state = "stopped"
            print(f"Process {pid} stopped.")
        else:
            print(f"No process with pid {pid} found.")

    def remove_process(self, pid):
        if pid in self.processes:
            del self.processes[pid]
            print(f"Process {pid} removed.")
        else:
            print(f"No process with pid {pid} found.")
