# app.py
import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Hello from my Python App in Docker!")
print(f"The current time is: {current_time}")
print(f"This is running inside a container built by Gishant!")
