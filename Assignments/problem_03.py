# Problem 3
# Create a number array([2,6,1,9,10,3,27])
# Get all items between 5 and 10 from it(including 5 and 10).
# #

import numpy as np

print("All items between 5 and 10 (including 5 and 10)(\"sorted\")")

# 1. populate the array.
a = np.array([2, 6, 1, 9, 10, 3, 27, 5])

# 2. sort the array first 
a = np.sort(a)

# 3. indexing the array.
b = a[(a >= 5) & (a <= 10)]

print("Result -> ", b)
