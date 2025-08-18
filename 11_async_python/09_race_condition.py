import threading
import time

chai_stock = 0

def restock():
    global chai_stock
    for _ in range(1_00_000):
        chai_stock += 1

threads = [threading.Thread(target=restock) for _ in range(2)]
for thread in threads: thread.start()
for thread in threads: thread.join()
print(f"Chai stock: {chai_stock}")