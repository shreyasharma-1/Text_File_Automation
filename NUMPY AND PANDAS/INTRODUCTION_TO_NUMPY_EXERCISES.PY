"""Q1)Create two dimensional 3*3 array and perform ndim, shape, slicing
operation on it. """ 
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Array:\n", arr)
print("Number of dimensions (ndim):", arr.ndim)
print("Shape of array:", arr.shape)

print("First row:", arr[0])         
print("First column:", arr[:, 0])   
print("Sub-array (first 2 rows, first 2 columns):\n", arr[:2, :2])
print("Last two elements of last row:", arr[2, 1:]) 

"""Q2)Create one dimensional array and perform ndim, shape, reshape operation
on it. """
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print("Original Array:", arr)

print("ndim (Number of Dimensions):", arr.ndim)
print("Shape:", arr.shape)

reshaped_arr = arr.reshape(2, 3)
print("\nReshaped Array (2x3):")
print(reshaped_arr)
print("ndim after reshape:", reshaped_arr.ndim)
print("Shape after reshape:", reshaped_arr.shape)
