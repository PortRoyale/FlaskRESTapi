import requests


BASE = "http://127.0.0.1:5000/"


data = [{'likes':68032, 'name':'Freedom Show', 'views':210503},
		{"likes":5643, "name":"Cheddar Cheese", "views":10598},
		{"likes":4361, "name":"Bears vs Packers", "views":93050}]

for i in range(len(data)):
	response = requests.put(BASE + "video/" + str(i), data[i])
	print(response.json())

input()
response = requests.get(BASE + "video/2") # sending helloworld because we added the resource to server of "helloworld"
print(response.json()) # need to decode it to readable format
input()

response = requests.patch(BASE + "video/2", {'likes': 55})
print(response.json())
