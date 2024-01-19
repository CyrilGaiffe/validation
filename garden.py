import threading

class Garden:
    def __init__(self):
        self.lock = threading.Lock()

    def enter_garden(self, name):
        with self.lock:
            print(f"{name} has entered the garden.")

    def leave_garden(self, name):
        print(f"{name} has left the garden.")
