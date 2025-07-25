import requests
from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv()

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key=os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
YOUR_WHATSAPP_NO="YOUR_WHATSAPP_NO (include '+country_code') "

weather_params={
    "lat":9.931233,
    "lon":76.267303,
    "appid":"1c2359aede14f9170c3388cbde95de62",
    "cnt":4,
}
will_rain=False
response=requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
data=response.json()
for hour_data in data["list"]:
    get_id=hour_data["weather"][0]["id"]
    if int(get_id)<700:
        print("It will rain")
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="Hi, I'm WETBOT, an AI Assistant designed by Mr. Abhijeet Nair.\nI wanna inform you that chances of Rain🌧️ are too high, in NEXT 12 HOURS. So, make sure you carry your umbrella☂️",
        to=f"whatsapp:{YOUR_WHATSAPP_NO}",
    )
print("Hello. This is my message. Successfully made an message bot. Thanks for your help")
print(message.status)



