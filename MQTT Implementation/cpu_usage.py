import psutil
import time

def monitor_mqtt_broker():
    broker_process_name = "mosquitto.exe"  # Change this if using a different broker

    while True:
        for process in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
            if broker_process_name in process.info['name']:
                print(f"MQTT Broker PID: {process.info['pid']}, CPU Usage: {process.info['cpu_percent']}%")
        time.sleep(2)  # Monitor every 2 seconds

monitor_mqtt_broker()
