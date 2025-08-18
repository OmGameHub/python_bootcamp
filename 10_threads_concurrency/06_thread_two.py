import threading
import time

def prepare_chai(chai_type, wait_time):
    print(f"Preparing {chai_type} chai...")
    time.sleep(wait_time)
    print(f"{chai_type} chai is ready.")

t1 = threading.Thread(target=prepare_chai, args=("Masala", 2))
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 3))

t1.start()
t2.start()

t1.join()
t2.join()

