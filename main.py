from Setup import Setup
from APIConnection import APIConnection
from neopixel import NeoPixel
from machine import Pin
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import time

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

    counter = 0
    danger_counter = 1
    grb_tuple = (0,0,0)

    button = machine.Pin(2,machine.Pin.IN, machine.Pin.PULL_UP)
    button_2 = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)

    I2C_ADDR = 39
    I2C_NUM_ROWS = 2
    I2C_NUM_COLS = 16

    sda = machine.Pin(0)
    scl = machine.Pin(1)
    i2c_controller = 0

    i2c = I2C(i2c_controller, sda=sda, scl=scl, freq=400000) 
    print(i2c.scan())
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

    dgr_str = ['', 'Alpine', 'Below', 'Tree']

    while True:
        
        if metadata.metadata[counter][danger_counter] == "Low":
            grb_tuple = (0,255,0)
        elif metadata.metadata[counter][danger_counter] == "Moderate":
            grb_tuple = (255,200,0)
        elif metadata.metadata[counter][danger_counter] == "Considerable":
            grb_tuple = (255,80,0)
        elif metadata.metadata[counter][danger_counter] == "High":
            grb_tuple = (255,0,0)
        else:
            grb_tuple = (48,25,52)

        np = NeoPixel(30,0,4,"GRB")
        np.fill(grb_tuple)
        np.show()
        
        elevation = ""

        if button.value() != 1:
            if counter == 2:
                counter = 0
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr(metadata.metadata[counter][0])
            else:
                counter = counter +1
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr(metadata.metadata[counter][0])
            danger_counter = 1


        if button_2.value() != 1:
            if danger_counter == 3:
                danger_counter = 1
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr(metadata.metadata[counter][0])
                lcd.move_to(0,1)
                lcd.putstr(metadata.metadata[counter][danger_counter])
            else:
                danger_counter = danger_counter+1
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr(metadata.metadata[counter][0])
                lcd.move_to(0,1)
                lcd.putstr(dgr_str[danger_counter] + metadata.metadata[counter][danger_counter])

        time.sleep(0.1)

if __name__ == "__main__":
    main()
