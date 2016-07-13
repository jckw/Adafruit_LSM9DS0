from __future__ import print_function

import Adafruit_LSM9DS0
import math
import time

# Create new LSM9DS0 instance
imu = Adafruit_LSM9DS0.LSM9DS0()

table = []

while True:
	# Get the values from the returned array/list
	(mag_x, mag_y, mag_z) = imu.rawMag()

	# Calculate the angle using basic trig
	angle_deg = math.degrees(math.atan2(mag_y, mag_x))

	# NOTE: this method does not account for tilt!
	print("Non-tilt: deg:", angle_deg)

	# Wait until repeating 
	time.sleep(0.05)





