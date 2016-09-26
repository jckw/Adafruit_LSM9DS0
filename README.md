# Adafruit LSM9DS0 Python Module
###### Designed for use with the Raspberry Pi, and Adafruit's LSM9DS0 breakout board

This is a basic Python module for use with Adafruit's LSM9DS0 breakout board. Reads byte data through I2C, for all the sensors available. 

The code is currently written for Python 2.7, since the Adafruit GPIO library is not written Python 3 (sadly). However, the code should work for Python 3 if Adafruit's library is made compatible; if not, with a few minimal changes. 

This is **raw data**, obviously – but there are some examples of how data can be fused/ used in the examples folder. Calibration is still needed.

Modifications and the ability to change more settings will (probably) come soon.

This project is licensed under the MIT license.

