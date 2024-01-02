import numpy as np
arr1 = np.random.randint(10, 100, 36).reshape(6,6)
print("Array Before splitting:\n",arr1)
arr2 = np.vsplit(arr1, 2)
lst = []
for i in arr2:
    lst += np.hsplit(i, 2)
arr3 = np.array(lst)
print("\nArray after splitting:\n", arr3)