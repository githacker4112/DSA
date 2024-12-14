import threading
import time

class MyThread(threading.Thread):
    def __init__(self, thread_name, delay):
        super().__init__()
        self.thread_name = thread_name
        self.delay = delay

    def run(self):
        print(f"Thread {self.thread_name} started")
        for i in range(5):
            time.sleep(self.delay)
            print(f"Thread {self.thread_name}: Count {i + 1}")
        print(f"Thread {self.thread_name} finished")

# Create thread instances
thread1 = MyThread("Thread-1", 1)  # Runs with 1-second delay
thread2 = MyThread("Thread-2", 2)  # Runs with 2-second delay

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All threads have completed.")