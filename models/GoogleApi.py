class GoogleApi:
    def __init__(self):
        with open('key.txt', 'r') as filename:  # open the key.txt file on local machine
            self.api_key = filename.read()  # set api_key to file content
        
        self.gmaps = googlemaps.Client(key=api_key)  # initialize googlemaps client

    def lookup(self, origin_in, destination_in, mode, choice):
        """Uses the GoogleMaps API to retrieve a JSON that contains the duration and distance between the origin_in and
        destination_in) """
        # print("Start lookup:", origin_in, destination_in, "with", mode, choice)
        origin = origin_in.replace(' ', '+')
        destination = destination_in.replace(' ', '+')
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'
        concat = url + "origins=" + origin + "&destinations=" + destination + "&key=" + api_key + "&mode=" + mode
        r = requests.get(concat)
        measurement = r.json()["rows"][0]["elements"][0][choice]["text"]

        return measurement