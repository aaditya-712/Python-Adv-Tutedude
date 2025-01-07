import urllib.request, urllib.parse, urllib.error

url = urllib.request.urlopen("http://127.0.0.1:5500/17_Web_Scraping/1_hello.html")

for line in url:
    print(line.decode().strip())