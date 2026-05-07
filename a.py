def calculate_product(numbers):
    # Initialize the result to 1 (the identity element for multiplication)
    product = 1
    for num in numbers:
        product *= num
    return product

# Defining your tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

# Calculating results
result1 = calculate_product(tup1)
result2 = calculate_product(tup2)

# Displaying the output
print(f"The product of tup1 is: {result1}")
print(f"The product of tup2 is: {result2}")