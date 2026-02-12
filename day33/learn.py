import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
print(response.status_code)
print(response.json())

latitude = response.json()['iss_position']['latitude']
longitude = response.json()['iss_position']['longitude']
print(latitude)
print(longitude)