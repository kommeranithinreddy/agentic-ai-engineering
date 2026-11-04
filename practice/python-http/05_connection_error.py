import httpx

def check_token(token : str, scheme : str = "Bearer") -> None:
    response = httpx.get("https://httpbin.org/bearer", headers = {"Authorization" : f"{scheme} {token}"})
    if response.status_code == 200:
        print("Request sent successfully")
        print(response.json())
    else:
        print('Rejected by server')
        print(f"Response code : {response.status_code}")


check_token("nithin123", "Basic")