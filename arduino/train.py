from serial import Serial
import time
arduino = Serial('/dev/cu.usbmodem1411', 250000)
time.sleep(2)

from flask import Flask, jsonify
from flask_cors import CORS

