from multiprocessing import Process, Queue

def prepare_chai(queue):
    print("Preparing chai...")
    queue.put("Chai is ready!")

def main():
    queue = Queue()
    process = Process(target=prepare_chai, args=(queue,))
    process.start()
    print(queue.get())
    process.join()

if __name__ == "__main__":
    main()