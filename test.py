from django import views
import requests


BASE = "http://127.0.0.1:5000/"


# data = [{"likes":335, "name":"tim","views":200000},
#         {"likes":40, "name":"John","views":300000},
#         {"likes":205, "name":"Flem","views":100000}]

# for i in range(len(data)):
#     response = requests.put(BASE+"video/" + str(i), data[i])
#     print(response.json())

# input()
# response = requests.delete(BASE + "video/0")
# print(response)

# input()

response = requests.patch(BASE + "video/2", {"views":99, "likes":101})
print(response.json())