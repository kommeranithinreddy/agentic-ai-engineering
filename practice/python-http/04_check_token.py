import httpx

response = httpx.get("https://httpbin.org/bearer", headers = {"Authorization": "Basic test123"})

print(response.status_code)
#print(response.json())