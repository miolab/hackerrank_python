import numpy as np

n, m = map(int, input().split())
arr = np.array([input().strip().split() for _ in range(n)], int)

print(arr.transpose(), arr.flatten(), sep='\n')
