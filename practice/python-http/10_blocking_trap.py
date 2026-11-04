import httpx, asyncio, time

async def get_fetch(client, url):
    response = httpx.get(url)
    return response

async def main():
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            get_fetch(client, "https://httpbin.org/delay/2"),
            get_fetch(client, "https://httpbin.org/delay/2"),
            get_fetch(client, "https://httpbin.org/delay/2")
            )
        for result in results:
            print(result.status_code)

start = time.perf_counter()
asyncio.run(main())

end = time.perf_counter()
print(end - start)