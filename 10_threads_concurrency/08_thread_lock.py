import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1_00_000):
        with lock:
            counter += 1


threads = [threading.Thread(target=increment) for _ in range(10)]
[i.start() for i in threads]
[i.join() for i in threads]

print(f"Final counter value: {counter}")