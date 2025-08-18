import threading
import requests
import time

def download_file(url):
    print(f"Starting download from {url}")
    response = requests.get(url)
    print(f"Finished download from {url}, size: {len(response.content)} bytes")


urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
]

def main():
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"All downloads completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
