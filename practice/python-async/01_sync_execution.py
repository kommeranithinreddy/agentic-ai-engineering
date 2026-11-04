import time

start = time.perf_counter()

def fetch_ai_response():
    print("Fetching AI response")
    time.sleep(3)
    print("AI response received")

def fetch_database_data():
    print("Fetching Database request")
    time.sleep(2)
    print("Databse data fetched")

fetch_ai_response()
fetch_database_data()

end = time.perf_counter()
print(end - start)