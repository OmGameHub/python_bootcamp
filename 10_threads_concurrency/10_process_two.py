from multiprocessing import Process
import time

def cpu_heavy():
    print("Crunching some numbers...")
    total = 0
    for i in range(10 ** 7):
        total += i

    print("Done crunching!")

def main():
    start_time = time.time()

    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [process.start() for process in processes]
    [process.join() for process in processes]

    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()