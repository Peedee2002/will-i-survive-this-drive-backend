import requests

url = "https://api.transport.nsw.gov.au/v1/traffic/historical"
headers = {'Authorization': 'apikey uRNmkPj7vvb45su3JWr4gZw88TiFHiaRgh9e'}

suburb="Kensington"
street="Anzac Parade"

body = {
  "region": "",
  "incident": "",
  "suburb": suburb,
  "street": street,
  "showHistory": True,
  "created": "2020-10-30",
  "end": "2020-12-30"
}

req = requests.post(url, headers=headers, json=body)
data = req.json()

hazard_list = data["result"]
crash = 0

# counts the num of crashes
for hazard in hazard_list:
    if (hazard["Hazards"]["features"]["properties"]["mainCategory"] == 'Crash'):
        crash += 1

print(crash)
