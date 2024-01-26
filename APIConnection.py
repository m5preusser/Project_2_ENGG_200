import urequests
import json, os

class APIConnection:

    # This 2D array contains all necessary metadata 
    # Each row represents a the information for that day
    # The first 3 rows have the following column structure:
    # Day of week, Alpine danger value, Below treeline danger value, Treeline danger value
    metadata = [
        ["","","",""],
        ["","","",""],
        ["","","",""]
    ]

    exposure = ""

    def get_api_data(self):

        url = "https://api.avalanche.ca/forecasts/en/products/point?lat=50.60737&long=-115.12578"

        response = urequests.get(url)

        for key, value in response.json().items():
            if key == "report":
                self.exposure = value["problems"][0]["factors"][1]["graphic"]["alt"]
                dangerRatings = value["dangerRatings"]
                for day in range(len(dangerRatings)):
                    self.metadata[day][0] = dangerRatings[day]["date"]["display"]
                    self.metadata[day][1] = dangerRatings[day]["ratings"]["alp"]["rating"]["display"]
                    self.metadata[day][2] = dangerRatings[day]["ratings"]["btl"]["rating"]["display"]
                    self.metadata[day][3] = dangerRatings[day]["ratings"]["tln"]["rating"]["display"]
                
