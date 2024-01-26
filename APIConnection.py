import urequests
import json, os

class APIConnection:

    def get_api_data(self):

        print("Called get_api_data")

        url = "https://api.avalanche.ca/forecasts/en/products/point?lat=50.60737&long=-115.12578"

        response = urequests.get(url)

        for key, value in response.json().items():
            if key == "report":
                print("Found the report")
                dangerRatings = value["dangerRatings"]
                for day in range(len(dangerRatings)):
                    print(dangerRatings[day].type())
