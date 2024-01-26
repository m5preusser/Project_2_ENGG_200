import network
import ubinascii
import time
import machine

class Setup:

    def connect(self):
        
        ssid = "airuc-guest"
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid)

        while wlan.isconnected() == False:
            print("Waiting for connection...")
            time.sleep(1)

    def setup(self):
        
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
        print(mac) 
