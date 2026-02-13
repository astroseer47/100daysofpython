import requests

ENDPOINT = ""
API_KEY = ""

prompt = input("Tell me what exercise you did:")
print(prompt)

try:
    response = requests.post(ENDPOINT, headers={"x-api-key": API_KEY})
    print(response.status_code)
    data = response.json()
except:
    data = prompt.split(" ")

with open("entry.txt","w") as f:
    f.write(str(data))
    f.write("\n")


