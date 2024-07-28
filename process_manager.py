import threading

class ProcessManager:
    def __init__(self):
        self.processes = {}

    def start_process(self, process_id, process_function, *args):
        if process_id in self.processes:
            print(f"Process {process_id} already running.")
        else:
            process_thread = threading.Thread(target=process_function, args=args)
            self.processes[process_id] = process_thread
            process_thread.start()
            print(f"Process {process_id} started.")

    def stop_process(self, process_id):
        if process_id in self.processes:
            # This is a simplified approach. To stop a thread, you would need to use a proper mechanism.
            print(f"Stopping process {process_id} is not implemented in this simple version.")
        else:
            print(f"Process {process_id} not found.")
