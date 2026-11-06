from dotenv import load_dotenv
import os

load_dotenv()

app_name = os.environ["APP_NAME"]
app_env = os.environ["APP_ENV"]

print(app_name)
print(app_env)