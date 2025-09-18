# Numpy -> Numerical Python is a library -> core library of python
# pip install numpy


import numpy as np

# #Create a 1D array
arr1 = np.array([1,2,3])
# print(arr1)
# print(type(arr1))
# print(len(arr1))
# print(arr1[1])
# print(arr1[0:])

# #functions
# print(np.zeros(6))  #zeros array
# print(np.ones(5))   #ones array
# print(np.empty(4))  #empty array              #every time comes a differnt value why?
# print(np.arange(10))  #range
# print(np.arange(2,20))  #specific range
# print(np.arange(2,20,3))  #specific range withy specific interval
# #table of 9
# print(np.arange(9,99,9))
# print(np.linspace(0,20, num=5))   #specific line space/specific interval
# print(np.ones(20, dtype=np.int64)) #specify datatype


#Array Functions
arr2 = np.array([10,65,8.5,89,24,75,43,76,1.2,0.6,79])
print(arr2)
arr2.sort()   #sort
print(arr2)
print(np.concatenate((arr1, arr2))) #concatenate


#Create a 2D array
arr3 = np.array([[1,2,3,4,5],[5,4,3,2,1]])
print(arr3)
arr4 = np.array([[6,7,8,9,10],[10,9,8,7,6]])
print(arr4)
print(np.concatenate((arr3, arr4))) #concatenate
print(np.concatenate((arr3, arr4), axis=0)) #concatenate  y axis
print(np.concatenate((arr3, arr4), axis=1)) #concatenate  x axis

#Create a 3D array
arr5= np.array([[[0,1,2,3],[4,5,6,7]],[[0,1,2,3],[4,5,6,7]],[[0,1,2,3],[4,5,6,7]]])
print(arr5)
print(arr5.ndim)  #to find the number of dimensions
print(arr5.size)  # to find num of elements
print(arr5.shape)  # to find shape (dims,rows, cols)


#Reshape arrays 
arr6= np.array([1,2,3,4,5,6,7,8,9])
print(arr6)
print(arr6.reshape(3,3)) #3*3=9

#Convert 1D array into 2D array - row wise
arr7= np.array([1,2,3,4,5,6,7,8,9])
print(arr7)
print(arr7.shape)
arr8= arr7[np.newaxis, :]
print(arr8)
print(arr8.shape)

#Convert 1D array into 2D array - coloumn wise
arr9= np.array([1,2,3,4,5,6,7,8,9])
print(arr9)
print(arr9.shape)
arr10= arr9[:, np.newaxis]
print(arr10)
print(arr10.shape)


#array
a= np.array([1,2,3,4,5])
print(a)
print(a*3)
print(a+3)
print(a.mean())  #array mean
print(a.sum())  #array sum


