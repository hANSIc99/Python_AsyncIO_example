import time
import asyncio
import aiohttp


async def performGetRequest(session, url):
    async with session.get(url) as response:
        html = await response.text()
        if response.status == 200:
            return 'Successfully loaded {}'.format(url)
        else:
            return 'Error loading {}'.format(url)


async def main():
    
    print('Start Async I/O Demo')

    myFavorateWebsites = [
        'https://openssssssource.com', # will cause an exception
        'https://python.org',
        'https://github.com',
        'https://en.cppreference.com',
        'https://getfedora.org'
    ]

    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:

        tasks = [asyncio.create_task(performGetRequest(session, url)) for url in myFavorateWebsites]
        await asyncio.gather(*tasks, return_exceptions=True)
        
        results = []
        for task in tasks:
            try:
                results.append(task.result())
            except Exception as e:
                print('Exception occured: {}'.format(e))

        print('\n'.join(results))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())