# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:38:40 2020

@author: liamf
"""

import numpy as np
import cv2
import itertools
import csv
from collections import defaultdict
import os


import argparse
import Models , LoadBatches
from tensorflow.keras import optimizers
from tensorflow.keras.utils import plot_model

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

import tensorflow as tf
tf.test.is_gpu_available() # True/False




direct = '~/'
path = 'Dataset/Dataset/game4/Clip7/0177.jpg'


img = cv2.imread(os.path.join(direct,path), 1)
 #resize it 
img = cv2.resize(img, ( width , height ))
#input must be float type
img = img.astype(np.float32)


print("success")