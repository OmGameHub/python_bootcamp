import asyncio
import time

async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(2)
    # time.sleep(2)  # Simulating a blocking call
    print(f"{name} is ready!")

async def main():
    start_time = time.time()
    await asyncio.gather(
        brew("Masala chai"),
        brew("Coffee"),
        brew("Ginger Tea")
    )

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
