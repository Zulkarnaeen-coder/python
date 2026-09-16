import numpy as np

__ = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

_ = np.array([], dtype=int)
for i in __:
    if i % 2 != 0:
        _ = np.concatenate((_, np.array([-1])))
    else:
        _ = np.concatenate((_, np.array([i])))

print(f"Original Array : {__}")
print(f"The modified Array : {_}")

print(f'Original Shape : {__.shape}')

_2 = __.reshape(2,5)

print(f"2D Shape :{_2}")


s = 0
for x in __:
    if x % 2 ==0:
        s= s+x
print(f"The total sum of even numbers = {s}")
