import numpy as np

"""
array_2d = np.array((1,0,0),(0,1,0),(0,0,1, dtype=float)) is incorrect.
The paranthesis is incorrect the 2D data should be within [] separated
by commas and the datatype should be specified after the ] brackets separated
with a comma
"""

array_2d = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)], dtype=float)
print(
    "The syntax is incorrect with incorrect paranthesis () and incorrect "
    "dtype specified within the paranthesis of last row of elements"
)
print(
    "The correct syntax is array_2d = np.array([(1,0,0),(0,1,0),(0,0,1)], dtype=float)"
)
print("Output 1: ")
print(array_2d)

"""
creates a 1D array with elements 0, 0, 0
"""
a = np.array([0, 0, 0])
print("Output 2a: ")
print("This is a 1-D Array")
print(a)

"""
creates a 2D array with elements 0, 0, 0 in 1 row and 3 columns
"""
a = np.array([[0, 0, 0]])
print("Output 2b: ")
print("This is a 2-D Array")
print(a)

"""
This creates an array of 48 evenly spaced values between 1 and 
48 (both inclusive). It divides the specified range into 48 equally
space points. reshape reshapes the array above into dimensions of 
3,4,4. A 3-d numpy array of dimensions 3x4x4 is created and filled
with evenly spaced numbers ranging from 1 to 48
"""
arr = np.linspace(1, 48, 48).reshape(3, 4, 4)
print("Output 3a: ")
print("This is a 3-D Array of 3X4X4")
print(arr)

# Prints element 20 from the array which is at 1 X 0 X 3
print("Output 3b: ")
print(arr[1, 0, 3])

# Prints elements 9.10.11.12 from the array which us at 0 X 2 and all 3
# columns indicated with :. flatten method prints it in output format
# requested
print("Output 3c: ")
print(arr[0, 2:3].flatten())

# Prints all elements from 33 until 48.
subset = arr[2::].reshape(4, 4)
print("Output 3d: ")
print(subset)

# Prints all elements in row1, cols 0 and 1 in all three dimensions
# which are [[5. 6.], [21. 22.] [37. 38.]]
print("Output 3e: ")
print(arr[0:3, 1, 0:2])

# Prints elements in row3,2 in reverse order in 2 dimension
# which are [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
subset = arr[2, 0:4, 2:4]
subset_reversed = subset[:, ::-1]
print("Output 3f: ")
print(subset_reversed)

# Prints all values in 0th column of all dimensions in reverse order
# which is [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]
subset = arr[0:3, 0:4, 0]
subset_reversed = subset[:, ::-1]
print("Output 3g: ")
print(subset_reversed.reshape(3, 4))

# Prints columns 0 and 3 in first row of 1st dimension and same columns in
# last dimension of last row which is [[1. 4.] [45. 48.]]
subset = arr[[0, 0, 2, 2], [0, 0, 3, 3], [0, 3, 0, 3]]
result = subset.reshape(2, 2)
print("Output 3h: ")
print(result)

# Print all elements from row 2 in 2nd dimension until end of array
# which has elements starting from 25 until 48
# Get all elements from 25 until 32 as arr1
arr1 = arr[1, 2:, :]

# Get all elements from 33 which is in 2nd dimension and all values
# reshape this to a 2D array of 4X4
arr2 = arr[2:, 0:2, :]
arr2 = arr2.reshape(2, 4)

# Join both these arrays to get a single array of 2D of all elements from
# 25 until 48 and print it
subset = np.vstack((arr1, arr2))
print("Output 3i")
print(subset)
