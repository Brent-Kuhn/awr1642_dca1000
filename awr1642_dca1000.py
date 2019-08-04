# Import necessary libraries for reading and converting data
import socket
import numpy as np
import logging as log
import threading
from queue import Queue

def readADC(nC):
    # nC is the Number of packets to buffer (default should be 3)

    # Make dynamic variables
    NS = 256    # Frame size
    adcData = [] # Empty array for storing returned adc data
    count = 0

    # Set IP and Port addresses to match the documentation
    UDP_IP = "192.168.33.30"
    UDP_PORT = 4098

    # Set socket number and the previous socket number to 0 
    # to initialize them as ints
    prevNum = 0
    sNum = 0

    while (count < nC):
        try:
            # Gather data from the DCA1000
            data, addr = sock.recvfrom(1500)

            # Check to see if data is in order
            sNum = int.from_bytes(data[0:4], byteorder = "little")
            if (sNum != 0 & prevNum != 0):
                if (sNum != (prevNum + 1)):
                    log.error("Socket out of order")
                    # Add zero filling for missing sockets

            # Find length of data
            sLen = int.from_bytes(data[4:10], byteorder = "little")

            # Extract the data from the socket
            sData = int.from_bytes(data[10:sLen+1], byteorder="litle", signed=True)

            # Append the new data to the adcData array
            adcData.append(sData)

            # Update the previus socket number to be the current socket number
            prevNum = sNum

        except:
            # Setup UDP socket protocol
            log.debug("Initializing socket bind")
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((UDP_IP, UDP_PORT))
            log.debug("Socket bind complete")

        finally:
            socket.close()
    
    return adcData