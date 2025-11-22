# importing helper functions
from helper_functions.run_bat_file import run_bat_file
from helper_functions.create_connection import wait_for_data_source

#Importing nessary libraries
import time
import socket

# Configuration
HOST = '127.0.0.1'  # Localhost (your own computer)
PORT = 30003        # The specific port for "BaseStation" (CSV) data

def main():
    """Initializes the ADS-B data collection by running the batch file and creates """

    process = None

    try:
        process = run_bat_file() # Run the batch file to start ADS-B data collection
        time.sleep(10)  # Wait for 10 seconds to ensure the batch file has started
        print("Batch file started successfully. Process ID:", process.pid)
        s = wait_for_data_source(HOST, PORT)  # Wait for the data source to be available
        print(f"Connected to ADS-B data stream at {HOST}:{PORT}")

        socket_file = s.makefile('r', encoding='utf-8')
        for line in socket_file:
            # Split the CSV data into a list
            data = line.strip().split(',')

            # Ensure we have enough columns to avoid errors
            if len(data) > 10:
                # Column 0 is the message type (e.g., "MSG")
                # Column 4 is the Hex ID (Unique Plane ID)
                # Column 11 is Altitude
                # Column 14 is Latitude
                # Column 15 is Longitude
                msg_type = data[0]
                hex_id = data[4]
                
                # Message Type 3 often contains Position data
                if msg_type == 'MSG' and data[14] != '' and data[15] != '':
                    lat = data[14]
                    lon = data[15]
                    alt = data[11]
                    print(data, ".....")
                    print(f"Plane {hex_id}: Alt {alt}ft @ {lat}, {lon}")
                
                # Message Type 1 often contains Callsigns (Flight Numbers)
                elif msg_type == 'MSG' and data[10] != '':
                    callsign = data[10]
                    print(data, ".....")
                    print(f"Plane {hex_id} is Flight: {callsign}")

    except ConnectionRefusedError:
        print("Error: Could not connect. Is Dump1090 running with --net?")
    except KeyboardInterrupt:
        print("\nStopping script...")
        process.terminate()
        s.close()

if __name__ == "__main__":
    main()