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
        'https://opensource.com',
        'https://python.org',
        'https://github.com',
        'https://en.cppreference.com',
        'https://getfedora.org'
    ]

    connector = aiohttp.TCPConnector(verify_ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:

        start = time.time()
        for url in myFavorateWebsites:
            result = await performGetRequest(session, url)
            print(result)
        end = time.time()
        print('>>> Elapsed time on synchronous access: {}'.format(end - start))

        start = time.time()
        tasks = [asyncio.create_task(performGetRequest(session, url)) for url in myFavorateWebsites]
        await asyncio.gather(*tasks)
        
        results = [task.result() for task in tasks]
        print('\n'.join(results))
        end = time.time()
        print('>>> Elapsed time on asynchronous access: {}'.format(end - start))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())