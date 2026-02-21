import os
import requests
from twilio.rest import Client



MY_LAT=30.101847
MY_LONG=31.262802
OWM_api_key=os.environ.get("OWM_API_KEY")

account_sid = "ACbbb87e044b0db1bbeea97ab09bc5b51a"
auth_token = os.environ.get("AUTH_TOKEN")



client = Client(account_sid, auth_token)




OWM_parameters = {
    "lat": -1.683500,
    "lon": 29.235600,
    "appid": OWM_api_key,
    "units": "metric",
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=OWM_parameters)
response.raise_for_status()

weather_data = response.json()



is_raining = False




for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <700:
        print("Bring an Umbrella")
        is_raining = True
        break

if is_raining:
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella ☔",
        from_="whatsapp:+14155238886",
        to="whatsapp:+201205978443",
    )
    print(message.status)

