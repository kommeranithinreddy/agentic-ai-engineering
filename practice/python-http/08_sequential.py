import httpx, time

start = time.perf_counter()

for _ in range(3):
    httpx.get("https://httpbin.org/delay/2")

end = time.perf_counter()
print(end - start)