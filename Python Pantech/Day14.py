#Numpy-indexing and slicing
import numpy as np
a=np.arange(10)
s=slice(2,7,2)
print(a[s])
b=a[2:7:2]
print(b)

"""
Numpy-Iterating over an array:
    1.Numpy conatins an iterator object nditer
    2.It is a multidimensional array object which is used to iterate over an object.
"""
a1=np.arange(0,60,5)
a1=a1.reshape(3,4)
print('Original Array is: ')
print(a1)
print('\n')
print('Modified array is: ')
for x in np.nditer(a1):
    print(x)

"""
Numpy-Array Manipulations
    1.A variety of routines are available in numpy package for manipulation of elements in ndarray object.
    2.Reshape-It gives a new shape to the object without changing its size.
    3.Flat-A one-D iterator over an array.
    4.Flattern-Returns a copy of an array compressed into a single-dimension.
    5.Ravel-Returns a continuous flattened array.
"""

"""
1.Trignometric functions which return trignometric ratios for a given angle in radians.
2.Arcsin,arcos and arctan return the inverse trignometric values of sin,cos and tan of given angle.
3.The result of these functions can be verified by numpy.degrees() function by converting radians to degree.
"""
