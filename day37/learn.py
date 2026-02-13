import requests
import datetime

params = {
    "token": "",
    "username": "",
}

payload = {
    "id": "",
    "name": "",
    "age": "",
    "gender": "",
    "today": datetime.datetime.now().strftime("%Y-%m-%d"),
}

headers = {
    "Content-Type": "application/json",
    "X-API-Key": ""
}

# POST
response = requests.post("http://127.0.0.1:8000/articles", json=payload, params=params, headers=headers)
response.raise_for_status()
data = response.json()
print(data)


# PUT
put_response = requests.put("http://127.0.0.1:8000/articles", json=payload, params=params, headers=headers)
put_response.raise_for_status()
data = put_response.json()
print(data)


# DELETE
delete_response = requests.delete("http://127.0.0.1:8000/articles/{}".format(data["id"]))
delete_response.raise_for_status()
data = delete_response.json()
print(data)
