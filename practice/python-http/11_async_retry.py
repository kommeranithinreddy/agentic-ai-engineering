import httpx
import time
import asyncio

async def get_with_retry(client : httpx.AsyncClient, url : str, maxattempts : int = 3) -> httpx.Response | None :
    attempt = 0
    print(f"This is for URL : {url}")
    for _ in range(maxattempts):
        attempt += 1
        try:
            response = await client.get(url, timeout = 2.0)
        except httpx.RequestError:
            print(f"Attempt number : {attempt}")
            if attempt == maxattempts:
                return None
            await asyncio.sleep(attempt * 2.0)
            continue
        
        if response.status_code == 200:
            return response

        elif response.status_code == 429 or response.status_code == 503:
            if attempt == maxattempts:
                print(f"{url}: gave up after {attempt} attempts")
                return None

            print(f"Attempt number : {attempt}")
            print(f"Status Code: {response.status_code}")
            await asyncio.sleep(attempt * 2.0)

            
        else:
            print(f"{url}: server answered {response.status_code}")
            print(f"{url}: gave up after {attempt} attempts")
            return response



url1 = "https://httpbin.org/status/200"
url2 = "https://httpbin.org/status/503"
url3 = "https://httpbin.org/status/404"
url4 = "https://httpbin.org/bearer"
url5 = "https://httpbin.org/delay/5"
url6 = "https://httpbin.org/status/500"


async def main():
    async with httpx.AsyncClient() as client:
        result = await asyncio.gather(
        get_with_retry(client, url1),
        get_with_retry(client, url2),
        get_with_retry(client, url3),
        get_with_retry(client, url4),
        get_with_retry(client, url5),
        get_with_retry(client, url5))
        print(result)


start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()
print(end - start)
