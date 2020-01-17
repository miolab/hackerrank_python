import numpy as np

arr = np.array((input().split()), float)
np.set_printoptions(sign=' ')

print(np.floor(arr), np.ceil(arr), np.rint(arr), sep = "\n")