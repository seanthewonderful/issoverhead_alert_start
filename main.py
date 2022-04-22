import requests
from datetime import datetime
import smtplib


MY_LAT = 40.346401
lat_x = MY_LAT - 5
lat_y = MY_LAT + 5
MY_LON = -111.910072
lon_x = MY_LON - 5
lon_y = MY_LON + 5

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def iss_overhead():
    if lat_x <= iss_latitude <= lat_y and lon_x <= iss_longitude <= lon_y:
        if time_now.hour < sunrise or time_now.hour > sunset:
            print("It's dark, you can see the ISS above you.")
            return True
        else:
            print("The ISS is above you, but it's light outside.")
            return False

    else:
        print("ISS is not above you now.")
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
# API only serves UTC time...don't have time to reprogram it but you get the gist
time_now = datetime.now()
print(time_now.hour)
print(sunrise)
print(sunset)
print(data["results"]["sunrise"])
print(data["results"]["sunset"])
# iss_overhead()

if iss_overhead():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login("bigbirthdaybuddyboy@gmail.com", "9Pythons")
        connection.sendmail(from_addr="bigbirthdaybuddyboy@gmail.com", 
                            to_addrs="seanthewonderful@gmail.com",
                            msg=f"Subject: ISS Overhead\n\nThe ISS is overhead now, and my calculations indicate that with a clear sky you can see it right now.")


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



