import time
import requests
from datetime import datetime
import smtplib

MY_EMAIL="MY_EMAIL"
MY_PASSWORD="MY_PASSWORD"
MYLAT=8.9806
MYLOG=38.7578

def overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()

    iss_lat=float(data["iss_position"]["latitude"])
    iss_lng=float(data["iss_position"]["longitude"])

    if 8.9806 - 5 <= iss_lat <= 8.9806 + 5 and 38.7578 - 5 <= iss_lng <= 38.7578 +5:
        return True




def is_night():
    parametrs = {
        "lat": MYLAT,
        "lng": MYLOG,
        "formatted": 0}
    request=requests.get("https://api.sunrise-sunset.org/json",params=parametrs)
    request.raise_for_status()
    data=request.json()

    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    print(sunset)
    print(sunrise)

    time=datetime.utcnow().hour
    if time>= sunset or time<= sunrise:
        return True

while True:
    time.sleep(60)
    if is_night() and overhead():
        connection=smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg='subject: Look Up \n\n ISS is above you in the sky')


