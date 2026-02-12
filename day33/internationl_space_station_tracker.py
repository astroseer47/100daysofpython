import requests
import datetime

from day32.main import send_email

MY_LAT =   51.507351
MY_LONG = -0.127758


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}



def is_night():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']

    print(sunrise)

    sunrise_split = sunrise.split("T")
    sunrise_time_split = sunrise_split[1].split(":")
    sunrise_time = int(sunrise_time_split[0])

    sunset_split = sunset.split("T")
    sunset_time_split = sunset_split[1].split(":")
    sunset_time = int(sunset_time_split[0])

    time_now = datetime.datetime.now().hour
    if time_now >= sunset_time or time_now <= sunrise_time:
        return True

    return False

def is_station_overhead():
    station_response = requests.get(url="http://api-open-notify.org/station_station")
    station_response.raise_for_status()
    data = station_response.json()

    station_latitude = float(data['results'][0]['latitude'])
    station_longitude = float(data['results'][0]['longitude'])


    if MY_LAT - 5 <= station_latitude <= MY_LAT + 5 and MY_LONG - 5 <= station_longitude <= MY_LONG + 5:
        return True
    return False


if is_night() and is_station_overhead():
    send_email(to_name="", to_address="",subject="Lookup", message="Station is above you in the sky")