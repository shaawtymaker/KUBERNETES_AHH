import psutil
import time

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    with open("/path/to/cpu_usage.log", "a") as f:
        f.write(f"CPU Usage: {cpu_usage}%\n")
    time.sleep(60)  # Wait for 60 seconds before the next check