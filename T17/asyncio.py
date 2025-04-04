import asyncio

async def fetch_data():
    print('Fetching data...')
    await asyncio.sleep(2)  # symulacja operacji I/O
    print('Data fetched')
    return {'data': 'example'}

async def main():
    data = await fetch_data()
    print(data)

asyncio.run(main())


