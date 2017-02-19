from serial import Serial
import time

arduino = Serial('/dev/cu.usbmodem1411', 250000)
time.sleep(2)

arduino.write(b'backward_on\n')
time.sleep(0.05)
arduino.write(b'backward_off\n')
time.sleep(0.05)