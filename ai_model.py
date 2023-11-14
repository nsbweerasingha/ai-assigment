!pip install numpy

!pip instal tensonflow

import numpy as np

# first neural network with keras tutorial
from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

dataset = loadtxt('/content/drive/MyDrive/AI/diabetes_without_header.csv',delimiter=',')

print(dataset)

x = dataset[:,0:8]