import numpy as np

"""
defining an array
arguments to the array must be something numpy can can turn into an array
"""
defined_array = np.array([1,2,3,4])

"""
3 most common array properties
1) size
    number of elements in the array
2) shape
    dimensions of the array like a vector or matrix. 
    defined_array has 4 elements along the frist dimension (4,)
3) data type
    data types in the array, defined_array is full of ints so its (int64)
    you can specify what dtype the array should be like
    new_array = np.array([1,2,3,4], dtype='float64')
"""
print(defined_array.size, defined_array.shape, defined_array.dtype, sep="------")

"""
creating a matrix (2 dimensional array)
"""

matrix_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype="float64")

print(matrix_array.size, matrix_array.shape, matrix_array.dtype, sep="----")

# stopped at page 35