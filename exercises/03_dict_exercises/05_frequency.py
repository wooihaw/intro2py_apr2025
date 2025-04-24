# Write a Python script to find the frequency of occurance for each alphabet in a string.
astring = 'A quick brown fox jumps over the lazy dog.'

# Only consider alphabets and convert them to lowercase
alist = [c.lower() for c in astring if c.isalpha()]

# Use for loop
freq = {}
for c in sorted(set(alist)):
    freq[c] = alist.count(c)
print(freq)

# Use dictionary comprehension
freq2 = {c: alist.count(c) for c in sorted(set(alist))}
print(freq2)
print(len(freq2))