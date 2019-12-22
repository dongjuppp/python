import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

h1 = np.array([[2, 2], [5, 6]])
h2 = np.array([[2, 4], [1, 6]])

print("h1*h2={}".format(h1*h2))
print("h1과 h2의 행렬의 곱={}".format(np.dot(h1, h2)))
