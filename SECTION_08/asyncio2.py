import time
import asyncio
import threading

async def getpage(url):    
    #time.sleep(1)   # 동기 대기
    await asyncio.sleep(1) # 비동기 대기
    print(f'complete {url}')

async def main():
    await asyncio.gather( getpage(1), getpage(2), getpage(3), 
                          getpage(4), getpage(5))

s = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

e = time.time()
print(e-s)