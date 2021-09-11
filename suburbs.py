import googlemaps
import json
from datetime import datetime


def get_suburbs(source, destination):

    gmaps = googlemaps.Client(key='AIzaSyB4ZJWZtLdjMPZtkUlCWbWGBNFvfuWq4dY')

    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions(source,
                                        destination,
                                        mode="driving",
                                        departure_time=now)

    suburb_result = []
    for step in directions_result[0]["legs"][0]["steps"]:
        start_lat = step["start_location"]["lat"]
        start_lng = step["start_location"]["lng"]
        end_lat = step["end_location"]["lat"]
        end_lng = step["end_location"]["lat"]

        reverse_start = gmaps.reverse_geocode((start_lat, start_lng))
        res_street = list(filter(lambda a: "route" in a["types"], reverse_start[0]["address_components"]))
        res_suburb = list(filter(lambda a: "locality" in a["types"], reverse_start[0]["address_components"]))
        if res_street and res_suburb:
            suburb_result.append(
                {
                    "suburb" : res_suburb[0]["long_name"],
                    "street" : res_street[0]["long_name"]
                }
            )

        reverse_end = gmaps.reverse_geocode((end_lat, end_lng))
        res_street1 = list(filter(lambda a: "route" in a["types"], reverse_end[0]["address_components"]))
        res_suburb1 = list(filter(lambda a: "locality" in a["types"], reverse_end[0]["address_components"]))
        if res_street1 and res_suburb1:
            suburb_result.append(
                {
                    "suburb" : res_suburb1[0]["long_name"],
                    "street" : res_street1[0]["long_name"]
                }
            )
            

    return suburb_result
