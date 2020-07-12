import requests


BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"likes":10, "name":"Freedom Show", "views":990}) # sending helloworld because we added the resource to server of "helloworld"
print(response.json()) # need to decode it to readable format
input() # pause cmd line
response = requests.get(BASE + "video/1") # sending helloworld because we added the resource to server of "helloworld"
print(response.json()) # need to decode it to readable format