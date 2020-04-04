import requests 
import json

r = requests.get("https://coronavirus-tracker-api.herokuapp.com/v2/locations")
data = json.loads(r.text)

total_confirmed = data["latest"]["confirmed"]
total_confirmed_ma = "N/A"
last_updated = "N/A"

for x in data["locations"]:
    if x["country_code"] == "MA":
        total_confirmed_ma = x["latest"]["confirmed"]
        last_updated = x["last_updated"]
        break

print("World: " + str(total_confirmed) + " cases / MA: " + str(total_confirmed_ma) + " cases")

