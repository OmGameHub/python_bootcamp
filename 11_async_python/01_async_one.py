import asyncio

async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(2)
    print("Chai is ready!")

def main():
    asyncio.run(brew_chai())

if __name__ == "__main__":
    main()