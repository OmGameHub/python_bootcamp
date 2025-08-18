import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} is brewing chai...")
    count = 0
    for _ in range(10_00_00_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing chai.")

thread1 = threading.Thread(target=brew_chai, name="Chai Maker 1")
thread2 = threading.Thread(target=brew_chai, name="Chai Maker 2")

start_time = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end_time = time.time()

print(f"Total time taken: {end_time - start_time:.2f} seconds")