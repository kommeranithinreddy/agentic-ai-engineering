import os

print(os.environ.get("APP_NAME", "default_return"))

appname = os.environ["APP_NAME"] #Raises error if APP_NAME not exists
print(appname)