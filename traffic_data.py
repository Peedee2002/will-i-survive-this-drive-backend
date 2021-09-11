import requests
import json
from time import sleep

def getAllTrafficOnRoute(route):
  total = 0
  for dict in route:
    try: 
        total += getTrafficPerHour(dict['street'], dict['suburb'], 'AM PEAK')
    except:
        total += 200
    sleep(0.2)
 
  return total

def getTrafficPerHour(street, suburb, period):
    '''
    Period is either : PM PEAK, AM PEAK, ALL DAYS, WEEKDAYS - play with these if you want to massage data or attempt to find data. 
    leave as None if you dont care
    '''
    url = 'https://api.transport.nsw.gov.au/v1/roads/spatial'
    headers = {'Authorization': 'apikey uRNmkPj7vvb45su3JWr4gZw88TiFHiaRgh9e'}
    addStr = ''
    if period is not None:
        addStr = f"AND PERIOD = '{period}'"

    query = f"SELECT NAME,LGA,SUBURB, TRAFFIC_COUNT, DATA_START_DATE, DATA_END_DATE, PERIOD FROM road_traffic_counts_station_reference \
        REF JOIN road_traffic_counts_yearly_summary SUMM ON REF.STATION_KEY = SUMM.STATION_KEY \
        WHERE NAME = '{street}' AND SUBURB = '{suburb}'" + addStr

    req = requests.get(url,params={'q': query}, headers=headers)
    myjson = json.loads(req.text)
    return myjson["rows"][0]["traffic_count"]

if __name__ == '__main__':
    print(getTrafficPerHour('Heathcote Road', 'Holsworthy', None))
