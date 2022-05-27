import os

import googlemaps
import requests
from logic.helpers import debug

from models.Timer import Timer

if os.path.exists("./models/secret.py"):
    from .secret import *
else:
    API_KEY = os.environ["API_KEY"]


class GoogleApi:
    def __init__(self):
        self.api_key = API_KEY
        self.gmaps = googlemaps.Client(key=self.api_key)  # initialize googlemaps client
        print("OK")

    def lookup(self, origin_in, destination_in, mode, choice):
        """Uses the GoogleMaps API to retrieve a JSON that contains the duration and distance between the origin_in and
        destination_in)"""
        with Timer("google api lookup") as lookup_timer:
            # print("Start lookup:", origin_in, destination_`in, "with", mode, choice)
            # debug(origin_in, destination_in)
            origin = origin_in.replace(" ", "+")
            destination = destination_in.replace(" ", "+")
            url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
            concat = f"{url}origins={origin}&destinations={destination}&key={self.api_key}&mode={mode}"
            # print(concat)
            r = requests.get(concat)
            measurement = r.json()["rows"][0]["elements"][0][choice]["text"]

            return measurement

    def namelookup(self, search, mode="driving", choice="distance"):
        """Uses the GoogleMaps API to retrieve a JSON that contains the searched name, then use this for lookup)"""
        with Timer("google api name_lookup") as lookup_timer:
            origin = search.replace(" ", "+")
            destination = search.replace(" ", "+")
            url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
            concat = f"{url}origins={origin}&destinations={destination}&key={self.api_key}&mode={mode}"
            # print(concat)
            r = requests.get(concat)
            name = r.json()["destination_addresses"][0]

            return name
