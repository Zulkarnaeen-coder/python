
ms = {1, 2, 3}
print(ms)


ms = {1.0, "Hello", (1, 2, 3)}
print(ms)


ms = {1, 2, 3, 4, 3, 2}
print(ms)


ms = set([1, 2, 3, 2])
print(ms,"\n")

#remove a number from a set
ns = set([0, 1, 3, 4, 5])
print("Original set:",ns)

ns.pop()
print("After removing the first element from the said set:")
print(ns,"\n")