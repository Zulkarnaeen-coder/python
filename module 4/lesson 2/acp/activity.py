def calc(n):
    product = 1
    for i in n:
        product*=i

    return product

t =(4,3,2,2,-1,18)
t2=(2,4,8,8,3,2,9)

new_t = calc(t)
new_t2 = calc(t2)

print(f"The result of tuple1= {new_t}")
print(f"The result of tuple2= {new_t2}")