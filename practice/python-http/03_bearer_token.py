import httpx

response = httpx.get("https://httpbin.org/bearer", headers = {"Authorization" : "Bearer nithin123"})

print(response.status_code)
print(response.json())