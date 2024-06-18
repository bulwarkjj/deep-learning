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
#print(defined_array.size, defined_array.shape, defined_array.dtype, sep="------")

"""
creating a matrix (2 dimensional array)
OUTPUT of .shape()
    the number of ints in the output tells the array dimensions so, (2,2,3) would be a 3 dimension array
    outut goes row-column-depth so (2,2,3) is 2 rows-2 columns-3 depth

"""

matrix_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype="float64")

#print(matrix_array.size, matrix_array.shape, matrix_array.dtype, sep="----")

"""
you can initalize every array element to 0 or 1 with .zeros() or .ones()
    this is useful if you want to build a large array but don't want to input every element
    it's a fast array build to manipulate later
    you input the row, column, depth you want
    input has to be a tuple so use () around input inside the method ()
you can input values other then 0 or 1 by prefixing multiplaction (can only be done with 1's due to 0xanyting=0)
"""
all_zero_array = np.zeros((2,3,4), dtype="uint32")
#print(all_zero_array)
#print(all_zero_array.shape, all_zero_array.size, sep="\n")
all_ten_array = 10*np.ones((2,2), dtype="uint32")
#print(all_ten_array)

"""
astype() method returns a copy of the array casting each element to the given data type
    you can also copy arrays by using .copy() method
"""
#print(all_ten_array.dtype)
copy_ten = all_ten_array.astype("uint8")
#print(copy_ten.dtype)

"""
arange() makes an array from the input argument
"""
a = np.arange(10)
print(a)

# stopped on page 37- Accessing elements in an array