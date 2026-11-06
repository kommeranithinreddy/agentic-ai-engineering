import httpx
import time

def get_with_retry(url : str, maxattempts : int = 3) -> httpx.Response | None :
    attempt = 0
    for _ in range(maxattempts):
        attempt += 1
        try:
            response = httpx.get(url, timeout = 2.0)
        except httpx.RequestError as e:
            print(f"Attempt number : {attempt}")
            if attempt == maxattempts:
                return None
            time.sleep(attempt * 2.0)
            continue
        
        if response.status_code == 200:
            return response

        elif response.status_code == 429 or response.status_code == 503:
            if attempt == maxattempts:
                print(f"Max attempts reached {attempt}, Please try again")
                return 

            print(f"Attempt number : {attempt}")
            print(f"Status Code: {response.status_code}")
            time.sleep(attempt * 2.0)

            
    
        elif response.status_code == 401 or response.status_code == 404:
            print(f"Status code : {response.status_code}")
            print("Please try again")
            return response

        else:
            return response


url1 = "https://httpbin.org/status/200"
url2 = "https://httpbin.org/status/503"
url3 = "https://httpbin.org/status/404"
url4 = "https://httpbin.org/bearer"
url5 = "https://httpbin.org/delay/5"
url6 = "https://httpbin.org/status/500"

urls = [url1, url2, url3, url4, url5, url6]
for url in urls:
    print(f"This is for url : {url}")
    result = get_with_retry(url)
    if result is None:
        print("Gave up")
    else:
        print(result.status_code)
    print("-" * 20)
