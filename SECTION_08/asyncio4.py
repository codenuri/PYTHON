import requests
import asyncio
import time

async def getpage(url):
    req = await loop.run_in_executor(None, requests.get, url)
    html = req.text
    print(len(html))


async def main():
    await asyncio.gather( getpage("https://www.cnn.com"),
                    getpage("https://www.cnn.com"),
                    getpage("https://www.cnn.com"),
                    getpage("https://www.cnn.com"),
                    getpage("https://www.cnn.com")    )
    

s = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


e = time.time()

print(e - s)