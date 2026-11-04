import httpx

data = {
    "userId": 1, 
    "title": "learn http", 
    "completed": False
    }
print(type(data))
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json = data) #user json instead of data and check the respone in content-type

print(response.status_code)
print(response.json())
print(response.request.headers["content-type"])