import requests
import time

def getpage(url):
    req = requests.get(url) # λκΈ° μμ
    html = req.text
    print(len(html))

def main():
    getpage("https://www.cnn.com")
    getpage("https://www.cnn.com")
    getpage("https://www.cnn.com")
    getpage("https://www.cnn.com")
    getpage("https://www.cnn.com")

s = time.time()
main()
e = time.time()

print(e - s)