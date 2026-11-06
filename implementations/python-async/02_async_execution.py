import asyncio
import time

start = time.perf_counter()

async def fetch_ai_response():
    print("Fetching AI response")
    await asyncio.sleep(3)
    print("AI response received")

async def fetch_database_data():
    print("Fetching Database request")
    await asyncio.sleep(2)
    print("Databse data fetched")

async def main():
    await asyncio.gather(
        fetch_ai_response(),
        fetch_database_data()
    )

asyncio.run(main())

end = time.perf_counter()
print(end - start)