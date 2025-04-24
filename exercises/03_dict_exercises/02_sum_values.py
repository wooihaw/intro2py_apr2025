# Write a Python script to print the sum of all values in the dictionary where the values are numbers.
# Expected results:
# adict =  {'a': 66, 'b': 33, 'c': 39, 'd': 7, 'e': 80, 'f': 5, 'g': 9}
# Sum of all values in the dictionary: 239

adict =  {'a': 66, 'b': 33, 'c': 39, 'd': 7, 'e': 80, 'f': 5, 'g': 9}

# Use for loop
total = 0
for k in adict:
    total = total + adict[k]
print(total)

# Use list comprehension
print(sum([adict[k] for k in adict]))

# Use values() method
print(sum(adict.values()))