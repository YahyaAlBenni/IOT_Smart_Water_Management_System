# CoAP-Based Smart Water Management System

## Overview

This project implements a CoAP-based communication system to monitor water tank levels and turbidity using Python and the `aiocoap` library. The system consists of:

- A **controller** that sends sensor data (main tank level, house tank level, and turbidity) to the CoAP server.
- A **server** that stores the latest sensor values and provides them upon request.
- A **client** that retrieves and displays sensor data while providing notifications based on predefined conditions.

## Implementation Steps

### 1. Install Dependencies

Ensure you have Python installed along with the required `aiocoap` package:


pip install aiocoap
2. Implement the CoAP Server:
The server stores sensor data and updates notifications based on predefined thresholds. The server exposes four CoAP resources:

- /main_tank_level: Updates main tank water level.
- /house_tank_level: Updates house tank water level.
- /turbidity: Updates turbidity value.
- /sensor_data: Retrieves the latest sensor readings and notification status.


The notification system sets flags if:
- The main tank is nearly full (>=99%) or the house tank is low (<25%).
- The turbidity exceeds 50 NTU.

Run the server: python server.py

3. Implement the Controller
The controller simulates sensor readings by generating random values for:

main_tank_level (0-100%)
house_tank_level (0-100%)
turbidity (0-100 NTU)
It sends data to the CoAP server every 5 seconds.

Run the controller:

bash
Copy
Edit
python controller.py
4. Implement the Client
The client retrieves sensor data from the CoAP server every 5 seconds. It filters out the notification field and displays sensor values. If notifications exist, they are displayed as alerts.

Run the client:

bash
Copy
Edit
python client.py
Results and Observations
The system successfully transmits sensor data from the controller to the server and retrieves it using the client.
Notifications are generated correctly based on:
High main tank levels.
Low house tank levels.
High turbidity.
The system updates in real-time with minimal latency.
The CoAP protocol efficiently transfers data with low bandwidth usage.
