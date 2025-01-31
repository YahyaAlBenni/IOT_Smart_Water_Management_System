import psutil
import time

def monitor_cpu_usage(interval=1):
    while True:
        cpu_usage = psutil.cpu_percent(interval=interval)
        print(f"CPU Usage: {cpu_usage}%")
        time.sleep(interval)

if __name__ == "__main__":
    monitor_cpu_usage()
