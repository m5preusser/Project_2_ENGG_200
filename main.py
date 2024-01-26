
from Setup import Setup
from APIConnection import APIConnection

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
    
if __name__ == "__main__":
    main()
