import requests
from time import sleep

def getAllCrashesOnRoute(route):
  total = 0
  for dict in route:
    total += getCrashes(dict['street'], dict['suburb'])

  return total

def getCrashes(street, suburb):
  url = "https://api.transport.nsw.gov.au/v1/traffic/historical"
  headers = {'Authorization': 'apikey uRNmkPj7vvb45su3JWr4gZw88TiFHiaRgh9e'}

  body = {
    "region": "",
    "incident": "",
    "suburb": suburb,
    "street": street,
    "showHistory": True,
    "created": "2019-7-1",
    "end": "2019-9-1"
  }

  req = requests.post(url, headers=headers, json=body)
  data = req.json()

  hazard_list = data["result"]
  crash = 0

  # counts the num of crashes
  for hazard in hazard_list:
      if (hazard["Hazards"]["features"]["properties"]["mainCategory"] == 'Crash'):
          crash += 1
  return crash

          
if __name__ == "__main__":
  suburb="Kensington"
  street="Anzac Parade"
  print(getCrashes(street, suburb))
