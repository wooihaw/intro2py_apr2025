# In-class examples for Day 1
#%% Numeric data types
import sys
sys.set_int_max_str_digits(10000)
a = 1248597928293487592837459739080988972948798472191240918402
b = a ** 100
print(a, b, sep='\n')
print(a.__sizeof__())
print(b.__sizeof__())

c = 1234567890
d = 1_234_567_890
print(c, d, sep='\n')

#%% Binary and hexadecimal numbers
x = 0b10110101
y =0x123cafe
print(x, y, sep=', ')
print(bin(x), hex(y), sep=', ')

#%% Converting between different data types
a, b, c = 1, 2.3, '456'
print(type(a), type(b), type(c), sep=', ')

d, e, f = float(a), str(b), int(c)
print(type(d), type(e), type(f), sep=', ')

x = '123abc'
print(x, type(x), sep=', ')
y = int(x, base=16)
print(y, type(y), sep=', ')

#%% Arithmetic operators
a = 3 ** 2
b = -3 ** 2
c = (-3) ** 2
print(a, b, c, sep=', ')

d = 2 ** 3 ** 2  # evaluated from right to left
e = (2 ** 3) ** 2
print(d, e, sep=', ')

#%% Comparison operators
a = 10
b = 25
print(a < b)
print(a > b)
print(a == b)
print(a != b)

print(0 <= a < 20)

#%% Walrus operator
# Old way
name = input("Enter your name: ")
if name != '':
    print(f"Hello {name}!")

# New way
if (name:=input("Enter your name: ")) != '':
    print(f"Hello {name}!")

#%% Raw string
path = r'C:\Users\wooihaw\python_venv\intro2py'
print(path)

#%% String indexing and slicing
s = "Introduction to Python"
print("First character:", s[0])
print(f"Last character: {s[-1]}")

print("First 5 characters:", s[:5])
print("Last 6 characters:", s[-6:])
print("Reversed string:", s[::-1])

#%% String concatenation and repetition
a = '123'
b = '4567'
c = '90'
print(a + b + c)

print(20 * "-", "Welcome", 20 * "-", sep='')

#%% String methods
s = "Introduction to Python"
print(s.lower())
print(s.upper())
print(s.title())
print(s.replace('Python', 'C++'))
print(s)

t = s.upper().replace('N', 'm').split()  # chaining string methods (left to right)
print(t)

#%% f-string formatting
a = 12.645
b = 0.0525
c = 67890

print(f'a = {a}, {a = }')
print(f'{a = :.0f}, {a = :.1f}, {a = :.2f}')

print(f"Percentage: {b:.2%}")

print(f"Binary: {c:b}, Hex: {c:x}")

#%% Getting input from the user
num = input("Enter an integer: ")
print(f"{num = }, {type(num) = }")
# print(f"10 times of {num} is {10 * num}")

if num.isdigit():
    print(f"10 times of {num} is {10 * int(num)}")
else:
    print(f"{num} is not an integer!")

#%% List join, append and extend
alist = [1, 2, 3]
print(f"{alist = }")

# Append new item
alist = alist + [4]
print(f"{alist = }")

alist += [5]
print(f"{alist = }")

alist.append(6)
print(f"{alist = }")

alist.extend([7, 8])
print(f"{alist = }")

alist.append([9, 10])
print(f"{alist = }")

print(f"{len(alist) = }")

#%% Sorting list
blist = [3, 4, 2, 6, 5, 0, 1]
clist = sorted(blist)  # sort in ascending order
dlist = sorted(blist, reverse=True)  # sort in descending order
print(f"{blist = }", f"{clist = }", f"{dlist = }", sep="\n")

elist = blist.sort(reverse=True)  # inplace sorting in descending order
print(f"{blist = }", f"{elist = }", sep="\n")

# flist = [1, 'abc', 2.5, [3, 4.5]]
# flist.sort()  # cannot sort list with a mixture of different data types

#%% List methods
alist = [1, 2, 3.4, 'abc', [5, 6.78], 'yz', 1, 'a']

print(f"{alist.count(1) = }")
print(f"{alist.count('a') = }")
print(f"{alist.index(1) = }")  # only return the index of the first item that matches the value

alist.remove(1)
print(f"{alist = }")

alist.insert(2, 5)  # insert the value 5 into position with index 2
print(f"{alist = }")

r = alist.pop(1)  # remove and return the item at index 1
print(f"{alist = }, {r = }")

#%% Tuple packing and unpacking
atuple = 1, 2.3, 4.5, 6, 7, 8, 9
print(f"{atuple = }, {type(atuple) = }")

first, *intermediate, last = atuple
print(f"{first = }, {intermediate = }, {last = }")









