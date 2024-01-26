
from Setup import Setup
from APIConnection import APIConnection

def main():
    print("Called Main")

    wifi_connection = Setup()
    wifi_connection.setup()
    
    try:
        wifi_connection.connect()
    except KeyboardInterrupt:
        wifi_connection.machine.reset()   

    metadata = APIConnection()
    metadata.get_api_data()

    
if __name__ == "__main__":
    main()
