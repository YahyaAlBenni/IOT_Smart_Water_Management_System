import aiocoap
import asyncio


async def get_sensor_data():
    context = await aiocoap.Context.create_client_context()
    while True:
        request = aiocoap.Message(code=aiocoap.GET, uri="coap://localhost/sensor_data")
        response = await context.request(request).response
        sensor_data = response.payload.decode()

        # Extract the relevant information from the response
        lines = sensor_data.strip().split('\n')
        tank_data_lines = [line for line in lines if "Notification" not in line]
        notification_line = [line for line in lines if "Notification" in line]

        # Print tank data excluding the notification field
        for line in tank_data_lines:
            print(line.strip())

        # Check for notification flag
        if notification_line:
            notification_value = int(notification_line[0].split(":")[1].strip())
            if notification_value == 1:
                print("Notification: Attention required for water level!")
            elif notification_value == 2:
                print("Notification: Attention required for turbidity!")
            elif notification_value == 3:
                print("Notification: Attention required for both water level and turbidity!")

        await asyncio.sleep(5)


async def main():
    await get_sensor_data()


if __name__ == "__main__":
    asyncio.run(main())





