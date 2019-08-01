# Import necessary libraries for reading and converting data
import socket
import numpy as np
import logging as log


def readADC():
    # Make dynamic variables
    NS = 256    # Frame size
    NC = 3      # Number of packets to buffer

    # Set IP and Port addresses to match the documentation
    UDP_IP = "192.168.33.30"
    UDP_PORT = 4098

    #set socket number and the previous socket number to 0 to initialize them as ints
    prevNum = 0
    sNum = 0

    # Setup UDP socket protocol
    log.debug("Initializing socket bind")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(UDP_IP, UDP_PORT)
    log.debug("Socket bind complete")

    while True:
        try:
            # Gather data from the DCA1000
            data, addr = socket.recvfrom(1500)

            # Check to see if data is in order
            sNum = int.from_bytes(data[0:4], byteorder = "little")
            if (sNum != 0 & prevNum != 0):
                if (sNum != (prevNum + 1)):
                    log.error("Socket out of order")
                    # Add zero filling for missing sockets

            # Find length of data
            sLen = int.from_bytes(data[4:10], byteorder = "little")

            # Extract the data from the socket\
            sData = int.from_bytes(data[10:sLen+1])

            # Update the previus socket number to be the current socket number
            prevNum = sNum

        finally:
            socket.close()
    
    return sData