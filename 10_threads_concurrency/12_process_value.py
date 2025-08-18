from multiprocessing import Process, Value

def increment(counter):
    for _ in range(1_00_000):
        with counter.get_lock():
            counter.value += 1

def main():
    counter = Value("i", 0)
    processes = [Process(target=increment, args=(counter,)) for _ in range(4)]
    [process.start() for process in processes]
    [process.join() for process in processes]
    print(f"Final counter value: {counter.value}")

if __name__ == "__main__":
    main()