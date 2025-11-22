import socket
import time
import sys

def wait_for_data_source(host, port, timeout_seconds=30, delay_seconds=2):
    """
    Attempts to connect to the specified host and port until successful 
    or the timeout is reached. Returns the connected socket object.
    """
    start_time = time.time()
    
    while time.time() - start_time < timeout_seconds:
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Attempt connection
            s.connect((host, port))
            
            # Connection successful!
            print(f"✅ Data source opened on {host}:{port}.")
            return s # Return the connected socket

        except ConnectionRefusedError:
            # Connection failed, wait and retry
            s.close()
            time.sleep(delay_seconds)
            
        except Exception as e:
            # Catch other potential socket errors
            s.close()
            print(f"  An unexpected error occurred during connection: {e}")
            sys.exit(1)

    # If the loop finishes without returning, the connection timed out
    print(f"Connection attempt timed out after {timeout_seconds} seconds. Exiting.")
    sys.exit(1)

