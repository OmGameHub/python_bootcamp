from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Starting to brew chai for {name}")
    time.sleep(2)
    print(f"Finished brewing chai for {name}")

def main():
    # create processes
    chai_makers = [
        Process(target=brew_chai, args=(f"Chat Maker #{i + 1}", ))
        for i in range(5)
    ]

    # Start all processes
    for maker in chai_makers:
        maker.start()

    # Wait for all processes to finish
    for maker in chai_makers:
        maker.join()

    print("All tasks completed.")

if __name__ == "__main__":
    main()