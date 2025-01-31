import aiocoap.resource as resource
import aiocoap
import asyncio

latest_sensor_data = {
    "main_tank_level": 0,
    "house_tank_level": 0,
    "turbidity": 0,
    "notification": 0
}

class SensorDataResource(resource.Resource):
    async def render_get(self, request):
        response_payload = f"""
        Main Tank Level: {latest_sensor_data["main_tank_level"]}%
        House Tank Level: {latest_sensor_data["house_tank_level"]}%
        Turbidity: {latest_sensor_data["turbidity"]} NTU
        Notification: {latest_sensor_data["notification"]}
        """
        return aiocoap.Message(payload=response_payload.encode())

def update_notification_status():
    notification = 0
    if latest_sensor_data["main_tank_level"] >= 99 or latest_sensor_data["house_tank_level"] < 25:
        notification |= 1  # Set the first bit if there's a tank level issue
    if latest_sensor_data["turbidity"] > 50:
        notification |= 2  # Set the second bit if there's a turbidity issue
    latest_sensor_data["notification"] = notification

class UpdateMainTankLevelResource(resource.Resource):
    async def render_put(self, request):
        latest_sensor_data["main_tank_level"] = float(request.payload.decode())
        update_notification_status()
        return aiocoap.Message(code=aiocoap.CHANGED)

class UpdateHouseTankLevelResource(resource.Resource):
    async def render_put(self, request):
        latest_sensor_data["house_tank_level"] = float(request.payload.decode())
        update_notification_status()
        return aiocoap.Message(code=aiocoap.CHANGED)

class UpdateTurbidityResource(resource.Resource):
    async def render_put(self, request):
        latest_sensor_data["turbidity"] = float(request.payload.decode())
        update_notification_status()
        return aiocoap.Message(code=aiocoap.CHANGED)

async def main():
    root = resource.Site()
    root.add_resource(['sensor_data'], SensorDataResource())
    root.add_resource(['main_tank_level'], UpdateMainTankLevelResource())
    root.add_resource(['house_tank_level'], UpdateHouseTankLevelResource())
    root.add_resource(['turbidity'], UpdateTurbidityResource())

    await aiocoap.Context.create_server_context(root, bind=("localhost", None))

    # This will keep the server running
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())






