import threading
import time

def boil_milk():
    print("Boiling milk...")
    time.sleep(2)
    print("Milk boiled.")

def toast_bun():
    print("Toasting bun...")
    time.sleep(1)
    print("Bun toasted.")

start_time = time.time()

milk_thread = threading.Thread(target=boil_milk)
bun_thread = threading.Thread(target=toast_bun)

milk_thread.start()
bun_thread.start()

milk_thread.join()
bun_thread.join()

end_time = time.time()
print(f"Breakfast is ready in {end_time - start_time:.2f} seconds")