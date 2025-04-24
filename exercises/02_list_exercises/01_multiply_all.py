# Write a Python script to multiply all the items in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -1]
print(f'{alist=}')

# Method 1 - Use for loop
result = 1
for n in alist:
    result = result * n
print(result)

# Method 2 - Use math module
from math import prod
print(prod(alist))