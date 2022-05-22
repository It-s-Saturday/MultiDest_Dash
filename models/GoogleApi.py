import os
import googlemaps
import requests


class GoogleApi:
    def __init__(self):
        key_path = os.getcwd() + "/models/key"
        with open(key_path, "r") as filename:  # open the key.txt file on local machine
            self.api_key = filename.read()  # set api_key to file content

        self.gmaps = googlemaps.Client(key=self.api_key)  # initialize googlemaps client
        print("OK")

    def lookup(self, origin_in, destination_in, mode, choice):
        """Uses the GoogleMaps API to retrieve a JSON that contains the duration and distance between the origin_in and
        destination_in)"""
        # print("Start lookup:", origin_in, destination_in, "with", mode, choice)
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
        origin = search.replace(" ", "+")
        destination = search.replace(" ", "+")
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
        concat = f"{url}origins={origin}&destinations={destination}&key={self.api_key}&mode={mode}"
        # print(concat)
        r = requests.get(concat)
        name = r.json()["destination_addresses"][0]
        return name
