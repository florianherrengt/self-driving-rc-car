import requests
from io import BytesIO
from PIL import Image
import numpy as np
from sklearn.externals import joblib

CAMERA_URL = 'http://192.168.1.211:8080/live.jpg'
ARDUINO_SERVER = 'http://localhost:5000'

clf = joblib.load('model.pkl')
print('model loaded')

def send_command(result):
    # requests.get('{}/stop'.format(ARDUINO_SERVER))
    print(result == 7)
    if result == 5:
        requests.get('{}/left-on'.format(ARDUINO_SERVER))
        requests.get('{}/forward-on'.format(ARDUINO_SERVER))
        return
    if result == 6:
        requests.get('{}/right-on'.format(ARDUINO_SERVER))
        requests.get('{}/forward-on'.format(ARDUINO_SERVER))
        return
    if result == 7:
        requests.get('{}/left-on'.format(ARDUINO_SERVER))
        requests.get('{}/backward-on'.format(ARDUINO_SERVER))
        return
    if result == 8:
        requests.get('{}/right-on'.format(ARDUINO_SERVER))
        requests.get('{}/backward-on'.format(ARDUINO_SERVER))
        return
    if result == 1:
        requests.get('{}/forward-on'.format(ARDUINO_SERVER))
    if result == 2:
        requests.get('{}/backward-on'.format(ARDUINO_SERVER))
    if result == 3:
        requests.get('{}/left-on'.format(ARDUINO_SERVER))
    if result == 4:
        requests.get('{}/right-on'.format(ARDUINO_SERVER))

def drive():
    response = requests.get(CAMERA_URL)
    img = Image.open(BytesIO(response.content)).convert('L')
    img_as_array = np.ndarray.flatten(np.array(img))
    result = clf.predict([img_as_array])[0]
    # print(result)
    send_command(result)
    drive()

print('start driving')
drive()

# r = requests.get('{}/left-on'.format(ARDUINO_SERVER))
# print(r)