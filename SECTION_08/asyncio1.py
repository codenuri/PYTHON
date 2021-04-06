import time

def getpage(url):
    time.sleep(1)   # download page
    print(f'complete {url}')

def main():
    getpage(1)
    getpage(2)
    getpage(3)
    getpage(4)
    getpage(5)


s = time.time()
main()
e = time.time()
print(e-s)