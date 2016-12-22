# Script that reads the temperature value from one of the GPIO pins and outputs
# the value to the terminal.
# Adapted in whole from
# https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/

# TODO(kfuruya) find the serial number of the probe with $ ls /sys/bus/wl/devices/

# Open the file
tfile = open("/sys/bus/w1/devices/$(SERIAL_NUMBER_OF_PROBE)/w1_slave") 
text = file.read()
tfile.close()
secondline = text.split("\n")[1]

temperaturedata = secondline.split(" ")[9]
temperature = float(temperaturedata[2:])
temperature = temperature/1000
print temperature
