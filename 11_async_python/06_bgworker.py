import asyncio
import threading
import time

def background_task():
    while True:
        time.sleep(1)
        print("Logging the system health...")

async def fetch_orders():
    await asyncio.sleep(3)
    print("🎁 order fetched")

def main():
    threading.Thread(target=background_task, daemon=True).start()
    asyncio.run(fetch_orders())


if __name__ == "__main__":
    main()