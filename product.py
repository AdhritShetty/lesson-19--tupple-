
x = int(input("x = "))

y = int(input("y = "))

z = int(input("z = "))

a = int(input("a = "))

b = int(input("b = "))

# Create a tuple with the numbers

tup2 = (x, y, z, a, b)

# Initialize product as 1

product = 1

# Multiply all numbers in the tuple

for num in tup2:

    product *= num

# Print the product

print("The product of the numbers is:", product)

