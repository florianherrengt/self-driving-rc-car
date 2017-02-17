from serial import Serial
import time
arduino = Serial('/dev/cu.usbmodem1411', 250000)
time.sleep(2)

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

arduino.write(b'forward_on\n')
time.sleep(0.1)
arduino.write(b'forward_off\n')
time.sleep(0.1)
arduino.write(b'backward_on\n')
time.sleep(0.1)
arduino.write(b'backward_off\n')
time.sleep(0.1)
arduino.write(b'left_on\n')
time.sleep(0.1)
arduino.write(b'left_off\n')
time.sleep(0.1)
arduino.write(b'right_on\n')
time.sleep(0.1)
arduino.write(b'right_off\n')

status = {
    'forward': False,
    'backward': False,
    'left': False,
    'right': False
}

@app.route("/status")
def get_status():
    return jsonify(status)

@app.route("/stop")
def stop():
    status['forward'] = False
    status['backward'] = False
    status['left'] = False
    status['right'] = False
    arduino.write(b'left_off\n')
    arduino.write(b'right_off\n')
    arduino.write(b'forward_off\n')
    arduino.write(b'backward_off\n')
    return "stop"

@app.route("/forward-on")
def forwardOn():
    status['forward'] = True
    arduino.write(b'forward_on\n')
    return "Forward on"

@app.route("/forward-off")
def forwardOff():
    status['forward'] = False
    arduino.write(b'forward_off\n')
    return "Forward off"

@app.route("/backward-on")
def backwardOn():
    status['backward'] = True
    arduino.write(b'backward_on\n')
    return "Backward on"

@app.route("/backward-off")
def backwardOff():
    status['backward'] = False
    arduino.write(b'backward_off\n')
    return "Backward off"

@app.route("/left-on")
def leftOn():
    status['left'] = True
    arduino.write(b'left_on\n')
    return "Left on"

@app.route("/left-off")
def leftOff():
    status['left'] = False
    arduino.write(b'left_off\n')
    return "Left off"

@app.route("/right-on")
def rightOn():
    status['right'] = True
    arduino.write(b'right_on\n')
    return "Right on"

@app.route("/right-off")
def rightOff():
    status['right'] = False
    arduino.write(b'right_off\n')
    return "Right off"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
