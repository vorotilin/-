import os
import sys
import webbrowser


def open_website(port=8000):  # default port
    """Opens the website in the default browser."""
    url = f'http://127.0.0.1:{port}/'
    
    try:
        webbrowser.open(url)
        print(f"Opened website at {url}")
    except webbrowser.Error:
        print(f"Could not open the browser. Make sure one is available, and that the server is running at {url}")


if __name__ == "__main__":
    # Set the desired port if the server is running on a different port
    port_number = 8000

    # Check if a specific port is given by the command-line arguments
    if len(sys.argv) > 1:
        try:
            port_number = int(sys.argv[1])
        except ValueError:
           print("Error: Invalid port provided as argument.")
           print(f"Usage: {os.path.basename(sys.argv[0])} [port_number]")
           sys.exit(1)
       
    open_website(port_number)






