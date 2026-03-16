import serial.tools.list_ports
import serial
import os
import time

from http.server import BaseHTTPRequestHandler, HTTPServer

SER = None

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global SER

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        url_content = self.path.replace('/', '')
        SER.write(bytes(url_content + '\n', 'utf-8'))

        r = SER.readline()
        print('Response', r)
        
        # Send the response body
        response_content = f"OK"
        self.wfile.write(response_content.encode("utf-8"))


def get_device_candidates():
    """
    Return a set of all available COM ports that have a valid Vendor ID (VID) and Product ID (PID).
    """
    ret = set()
    ports = serial.tools.list_ports.comports() # Get a list of all available ports
    if not ports:
        return ret

    for port in ports:
        # Check if the port has USB information (VID/PID)
        if port.vid is not None and port.pid is not None:
            ret.add(port)
    
    return ret

"""
    print(f"--- Port: {port.device} ---")
    print(f"Description: {port.description}")
    print(f"Hardware ID: {port.hwid}")
    
    # Check if the port has USB information (VID/PID)
    if port.vid is not None and port.pid is not None:
        # VID and PID are returned as integers by pyserial
        print(f"Vendor ID (VID): 0x{port.vid:04X} ({port.vid})")
        print(f"Product ID (PID): 0x{port.pid:04X} ({port.pid})")
"""


def exit_cleanly():
    raise UserWarning('Sup')

class MyHTTPServer(HTTPServer):
    def handle_error(self, request, client_address):
        print("Error occurred while communicating with device! Exiting")
        self.server_close()

def run_control_server(port):
    global SER
    s = serial.Serial(port.device, baudrate=115200, timeout=1)
    time.sleep(2)
    print('Connected!')

    SER = s
    host_name = "127.0.0.1"
    server_port = 8080
    web_server = MyHTTPServer((host_name, server_port), MyHandler)
    
    print(f"Server started http://{host_name}:{server_port}")
    print()
    print("=" * 80)
    print("Ready for RC commands!")
    print("=" * 80)

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass
    web_server.server_close()
    print("Server stopped.")

    exit_cleanly()


def attempt_connection(port):
    print('Trying to connect to device...', port.description)

    exited_cleanly = False
    try:
        run_control_server(port)
    except UserWarning:
        print('Control server exited - please restart this program to reconnect')
        exited_cleanly = True
    except Exception as e:
        print('Unexpected error occurred:', e)
        exited_cleanly = False
    return exited_cleanly


def main():
    candidates = get_device_candidates()
    best_candidates = []
    runner_ups = []
    for candidate in candidates:
        if candidate.vid in [0x1A86, 0x2E8A] and candidate.pid in [0x7523, 0x000A]:
            print('Found a supported device!')
            best_candidates.append(candidate)
        elif candidate.description.startswith('USB-SERIAL CH340') or candidate.description.startswith('USB Serial Device'):
            runner_ups.append(candidate)
    
    best_candidates = best_candidates + runner_ups

    n_devices = len(best_candidates)

    if n_devices == 0:
        print('No compatible device(s) found!')
        return
    else:
        print(f'{n_devices} device(s) found')
        for i in range(n_devices):
            exited_cleanly = attempt_connection(best_candidates[0])
            if exited_cleanly:
                break
    

if __name__ == "__main__":
    print('Working in:', os.getcwd())
    main()
    input('Press enter to close')
