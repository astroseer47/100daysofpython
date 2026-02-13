import requests
import twilio

API_KEY = "api-key-goes-here"
WEATHER_API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather?"
FORECAST_API_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast?"


TWILIO_API_ENDPOINT = ""
TWILIO_API_KEY = ""

weather_url="{}?q={}&units=metric&appid={}".format(WEATHER_API_ENDPOINT, API_KEY, API_KEY)

print(weather_url)
try:
    response = requests.get(weather_url)
    response.raise_for_status()
    response_json = response.json()
    print(response_json)
except:
    print("Error")


try:
    forecast_url="{}?lat={}&lon={}&cnt={}&appid={}".format(WEATHER_API_ENDPOINT, 57, -2.15,3 ,API_KEY, API_KEY)
    print(forecast_url)
    forecast_response = requests.get(forecast_url)
    forecast_response.raise_for_status()
    forecast_json = forecast_response.json()
    print(forecast_json)
except:
    print("Error")



# USING ENV
# export key_name=value
# os.environ.get(key_name)

# export WEATHER_API_ENDPOINT=api-endpoint-goes-here
# os.environ.get(WEATHER_API_ENDPOINT)



# try:
#     account_id = ''
#     token = ''
#     client = twilio.Client(account_id,token)
#     message = client.messages.create(
#         body="Hello world",
#         from="+12345567",
#         to="+33333333"
#     )
#     print(message.status)
# except:
#     print("Error")