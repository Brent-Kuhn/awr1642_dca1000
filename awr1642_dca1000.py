# Import necessary libraries for reading and converting data
import socket

# Set IP and Port addresses to match the documentation
UDP_IP = '192.168.33.30'
UDP_PORT = 4098

# Setup UDP socket protocol
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# For testing a file named test_data_x will be created and logged into
test_data_raw = open('test_data_raw.txt', 'w')
test_data_encoded = open('test_data_encoded.txt', 'w')

while True:
    try:
        # Gather data from the socket with port number 4096
        data, addr = socket.recvfrom(4096)
        # Print the data, will update to gather/convert/clean/organize
        print(data)
        # Write data to the raw file
        test_data_raw.write(data)
        # Just to see what this looks like as human readable
        stringData = data.decode('utf-8')
        # Print the encoded data, will update to gather/convert/clean/organize
        print(stringData)
        # Write data to the encoded file
        test_data_encoded.write(stringData)

    finally:
        socket.close()
        test_data_raw.close()
        test_data_raw.close()