import requests
import json
import os
city = input("Enter the country name and city or district name in country/city or district  format:\n")
url = f"https://api.weatherapi.com/v1/current.json?key=038129c2f2b140779f2164141230406&q={city}"
req=requests.get(url)
dic=json.loads(req.text)
d=dic["current"]["temp_c"]
e=dic["current"]["last_updated"]
say=f"according to our data updated at time {e} the temprature is {d} degree celcius"
command = f'''powershell -Command "(New-Object -ComObject SAPI.SpVoice).Speak('{say}')"'''
os.system(command)

