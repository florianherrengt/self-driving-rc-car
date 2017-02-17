
# coding: utf-8

# In[1]:

from PIL import Image
import requests
import numpy as np
from io import BytesIO
from os import listdir
from os.path import isfile, join
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split


# In[2]:

url = "http://images.nationalgeographic.com/wpf/media-live/photos/000/762/cache/panda-trees-woods-990-dl_76256_160x120.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content)).convert('L')


# In[3]:

np.ndarray.flatten(np.array(img))


# In[4]:

X = []
y = []


# In[5]:

images_left = [f for f in listdir('photos/left') if isfile(join('photos/left', f)) and f != '.DS_Store']
for i in images_left:
    X.append(
        np.asarray(
            np.ndarray.flatten(
                np.array(Image.open(join('photos/left', i)).convert('L'))
            )
        )
    )
    y.append(0)


# In[6]:

images_right = [f for f in listdir('photos/right') if isfile(join('photos/right', f)) and f != '.DS_Store']
for i in images_right:
    X.append(
        np.asarray(
            np.ndarray.flatten(
                np.array(Image.open(join('photos/right', i)).convert('L'))
            )
        )
    )
    y.append(1)


# In[7]:

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# In[8]:

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, random_state=1)


# In[9]:

clf.fit(X_train, y_train)


# In[10]:

clf.score(X_test, y_test)


# In[ ]:



