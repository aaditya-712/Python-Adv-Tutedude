import requests

url = "http://127.0.0.1:5500/17_Web_Scraping/1_hello.html"

# print(dir(requests))
response = requests.get(url = url)
print(response)
