# Import necessary libraries for reading and converting data
import socket
import numpy as np


def readADC():

    # Set IP and Port addresses to match the documentation
    UDP_IP = '192.168.33.30'
    UDP_PORT = 4098

    #set socket number and the previous socket number to 0 to initialize them as ints
    prevNum = 0
    sNum = 0

    # Setup UDP socket protocol
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # For testing a file named test_data_x will be created and logged into
    test_data_raw = open('test_data_raw.txt', 'w')
    test_data_int = open('test_data_int.txt', 'w')

    while True:
        try:
            # Gather data from the socket with port number 4096
            data, addr = socket.recvfrom(4096)

            # Check to see if data is in order
            sNum = int.from_bytes(data[0:4], byteorder = little)
            if (sNum != 0 & prevNum != 0):
                if (sNum != (prevNum + 1)):
                    print ("Socket out of order")
                    # Add zero filling for missing sockets

            # Find length of data
            sLen = int.from_bytes(data[4:8], byteorder = little)

            # Get byte count of ADC data
            adcLen = int.from_bytes(data[8:14], byteorder = little)



            # Print the data, will update to gather/convert/clean/organize
            print(data)
            # Write data to the raw file
            test_data_raw.write(data)
            # Just to see what this looks like as human readable
            stringData = int.from_bytes(data, byteorder = little)
            # Print the int data, will update to gather/convert/clean/organize
            print(stringData)
            # Write data to the int file
            test_data_int.write(stringData)

            # Update the previus socket number to be the current socket number
            prevNum = sNum

        finally:
            socket.close()
            test_data_raw.close()
            test_data_raw.close()