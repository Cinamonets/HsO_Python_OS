import platform

class SystemInfo:
    def get_info(self):
        """Zwraca informacje o systemie."""
        try:
            return {
                "system": platform.system(),
                "node_name": platform.node(),
                "release": platform.release(),
                "version": platform.version(),
                "machine": platform.machine(),
                "processor": platform.processor()
            }
        except Exception as e:
            print(f"Error retrieving system info: {e}")
            return {}
