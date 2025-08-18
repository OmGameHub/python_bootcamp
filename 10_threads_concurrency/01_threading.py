import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order {i}")
        time.sleep(1)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai {i}")
        time.sleep(2)

def main():
    # create threads
    order_thread = threading.Thread(target=take_orders)
    chai_thread = threading.Thread(target=brew_chai)

    # start threads
    order_thread.start()
    chai_thread.start()

    # wait for both threads to finish
    order_thread.join()
    chai_thread.join()

    print("All tasks completed.")

if __name__ == "__main__":
    main()