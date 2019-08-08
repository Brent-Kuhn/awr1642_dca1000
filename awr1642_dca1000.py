# Import necessary libraries for reading and converting data
import socket
import numpy as np
import logging as log
import threading
from queue import Queue

def readADC(nC):
    # nC is the Number of packets to buffer (default should be 3)

    # Make dynamic variables
    NS = 256        # Frame size
    adcData = []    # Empty array for storing returned adc data
    tempData = []   # Empty array for storing any temporary data

    log.basicConfig(level=log.DEBUG, format='%(message)s',)

    # Set IP and Port addresses to match the documentation
    UDP_IP = "192.168.33.30"
    UDP_PORT = 4098

    # Setup UDP socket protocol
    log.debug("Initializing socket bind.")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    log.debug("Socket bind complete.")

    try:
        for x in range(nC):
            # Gather data from the DCA1000
            data, addr = sock.recvfrom(1500)

            # Check to see if data is in order
            # Get the socket number
            sNum = int.from_bytes(data[0:4], byteorder="little")
            # Add zero filling for missing sockets

            # Find length of data
            sLen = len(data)

            sData = np.zeros((sLen-10)//2)

            # Extract the data from the socket
            for m,k in zip(range(10, sLen, 2), range(0,sLen-10)):
                binByte = int.from_bytes(data[m:m+2], byteorder="little", signed=True)
                sData[k] = binByte

            # Append the new data to the tempData array
            tempData.append([sNum, sData])

    except:
        log.debug("Socket connection seems to be lost or not found.")

    finally:
        sock.close()
        log.shutdown()
    
    # Sort the data according to the socket number
    tempData = sorted(tempData, key=lambda adcData: adcData[0])
    # Strip socket numbers so that only data is sent
    for i in range(len(tempData)):
        adcData.append(tempData[i][1])

    # Return only nC ammount of data as an array
    return adcData
