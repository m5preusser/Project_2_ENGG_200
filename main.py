from Setup import Setup
from APIConnection import APIConnection
from neopixel import NeoPixel
import time
from machine import Pin

def main():

    wifi_connection = Setup()
    wifi_connection.setup()
    
    try:
        wifi_connection.connect()
    except KeyboardInterrupt:
        wifi_connection.machine.reset()   

    metadata = APIConnection()
    metadata.get_api_data()

    for i in range(len(metadata.metadata)):
        print(metadata.metadata[i])
    
    print(metadata.exposure)
    print(metadata.summary) 

    np = NeoPixel(30,1,1)
    np.fill((255,0,0))
    np.show()
    print("done")
    
if __name__ == "__main__":
    main()
