mport serial
import time
import string
import pynmea2


port = "/dev/ttyAMA0"
ser = serial.Serial(port, baudrate=9600, timeout=0.5)
dataout = pynmea2.NMEAStreamReader()
while True:
        newdata = ser.readlines()
        for data in newdata:
                readable_data = data.decode('unicode_escape')
                if readable_data[0:6] == "$GPGGA":
                        newmsg = pynmea2.parse(readable_data)
                        lat = newmsg.lat
                        lon = newmsg.lon
                        alt = newmsg.altitude
                        sat = newmsg.num_sats
                        print("Num_Sat:" + str(sat) + " Lat=" + str(lat) + " long=" + str(lon) + " altitude=" + str(alt))
