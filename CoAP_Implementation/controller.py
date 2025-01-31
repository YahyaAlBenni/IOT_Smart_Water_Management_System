import aiocoap
import asyncio
import random

async def put_resource(uri, payload):
    context = await aiocoap.Context.create_client_context()
    request = aiocoap.Message(code=aiocoap.PUT, uri=uri, payload=payload.encode())
    response = await context.request(request).response
    print(f'Response: {response.code}')

async def main():
    while True:
        main_tank_level = str(random.randint(0, 100))  # Generate random value for main tank level
        house_tank_level = str(random.randint(0, 100))  # Generate random value for house tank level
        turbidity = str(random.uniform(0, 100))  # Generate random value for turbidity

        await put_resource("coap://localhost/main_tank_level", main_tank_level)
        await put_resource("coap://localhost/house_tank_level", house_tank_level)
        await put_resource("coap://localhost/turbidity", turbidity)

        await asyncio.sleep(5)  # Wait for 5 seconds before sending the next set of data

if __name__ == "__main__":
    asyncio.run(main())
