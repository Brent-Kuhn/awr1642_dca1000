# Import necessary libraries for reading and converting data
import socket

# Set IP and Port addresses to match the documentation
UDP_IP = '192.168.33.30'
UDP_PORT = 4098

# Setup UDP socket protocol
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Gather data from the socket with port number 4096
    data, addr = socket.recvfrom(4096)
    # Print the data, will update to gather/convert/clean/organize
    print(data)

finally:
    socket.close()