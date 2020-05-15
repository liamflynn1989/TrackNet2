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


direct = '~/'
path = '0001.jpg'


img = cv2.imread(os.path.join(direct,path), 1)

print("success")