"""
NumPy:
1.It stands for numerical python.
2.It is a library.It consists of multi-dimensional array objects and a group of routines for processing those arrays.
3.It is used to perform mathematical and logical operations on arrays.

Numpy-NDARRAY object
1.Important array object defined in Numpy is an n-dimensional array type called ndarray.
2.It describes the group of items of same type.
3.Each item in the collection cam be accessed using the zero-based index.
4.Every item in the ndarray occupies the same amount of memory.
5.Each elemenet in an ndarray is an object of data is called object(called dtype).
"""

import numpy as np
a=np.array([1,2,3])
print(a)

a2=np.array([1,2,3],dtype=complex)
print(a2)

a1=np.array([[1,2,5],[3,4,6]])
print(a1)
print(a1.shape)
print(a1.itemsize)
b=a1.reshape(3,2)
print(b)
print(b.shape)

p1=np.arange(24)
print(p1)
po=p1.reshape(2,4,3)
print(po)