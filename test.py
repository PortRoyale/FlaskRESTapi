import requests


BASE = "http://127.0.0.1:5000/"


data = [{'likes':10, 'name':'Freedom Show', 'views':990},
		{"likes":56, "name":"Free Cheese", "views":0},
		{"likes":6969, "name":"Your mommas tapes", "views":69}]

for i in range(len(data)):
	response = requests.put(BASE + "video/" + str(i), data[i])
	print(response.json())

input()
response = requests.get(BASE + "video/2") # sending helloworld because we added the resource to server of "helloworld"
print(response.json()) # need to decode it to readable format