import httpx

def check_status(token : str, scheme : str = "Bearer") -> None :
    try:
        response  = httpx.get(
            "https://httpbin.org/delay/3", 
            headers = {"Authorization" : f"{scheme} {token}"},
            timeout = 2.0
            )
        print(response.status_code)

    except httpx.RequestError as e:
        print(e)


check_status("nithin1234")