from multiprocessing import Process
import time

def crunch_number():
    print(f"Starting the count process...")
    count = 0
    for _ in range(10_00_00_000):
        count += 1
    print(f"Finished counting: {count}")

def main():
    start_time = time.time()

    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()