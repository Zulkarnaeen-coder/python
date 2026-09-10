import numpy as np

arr = np.array([2,3,11,3,4,2,5,2])
print(arr)
print(type(arr))



s = arr[0]
a=arr[1]
e=arr[2:5]
print(s)
print(a)
print(e)

arr2 = np.array([1,3,2,2,3,6,4,4,6,4,3,2,],dtype="S")
print(arr2)
print(arr2.dtype)



arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3)
print(arr3.shape)


arr4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr4)
print(arr4.reshape(3,4))

for _ in arr2:
    print(_)

arr5 =np.array([1,2,3,4,5,6,7,8,9])
asd = np.concatenate((arr5,arr4))
print(asd)