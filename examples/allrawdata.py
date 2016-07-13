import Adafruit_LSM9DS0

# Create new LSM9DS0 instance
imu = Adafruit_LSM9DS0.LSM9DS0()


print("Printing RAW accelerometer, gyroscope and magnetometer values...")

while True:
    # Get all data
    ACC = imu.rawAccel()
    GYR = imu.rawGyro()
    MAG = imu.rawMag()

    # Convert to strings for display
    strACC = ', '.join(str(num).rjust(5) for num in ACC)
    strGYR = ', '.join(str(num).rjust(5) for num in GYR)
    strMAG = ', '.join(str(num).rjust(5) for num in MAG)

    # Display in a pretty way
    print("Accel: " + strACC + " | Gyro: " + strGYR + " | Mag: " + strMAG)
