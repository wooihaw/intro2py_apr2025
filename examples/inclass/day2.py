# In-class examples for Day 2
#%% Dictionary  creation and modification
adict = dict(a=1, b=2.5, c='abc')
print(f"{adict = }")
print(f"{adict['c'] = }")

# print(f"{adict['d'] = }")  # KeyError is raised as the key 'd' is not found

# Use get() method to return a default value if the key is not found
print(f"{adict.get('d', 'No found') = }")
print(f"{adict = }")

# Use setdefault() method to insert the key and default value if the key is not found
print(f"{adict.setdefault('d', 5) = }")
print(f"{adict = }")

#%% Joining 2 dictionaries
d1 = {'a':1, 'b':2, 'c':3}
d2 = dict(x=4, y=5, z=6)
print(f"{d1 = }, {d2 = }")

# Method 1
d3 = d1.copy()
d3.update(d2)
print(f"{d3 = }")

# Method 2
d4 = d1 | d2
print(f"{d4 = }")

#%% Creating set
s1 = {1, 2, 4, 2, 0, 1, 2, 4, 9}
print(f"{s1 = }")

alist = ['apple', 'orange', 'apple', 'pear']
aset = set(alist)
print(f"{alist = }, {aset = }")

#%% Set methods
name1 = ['Ali', 'Baba', 'Cloud', 'Data', 'Engineer']
name2 = ['John', 'Appleseed', 'Engineer', 'Peter', 'Ali', 'Chan']

# Names common to both lists
common_names = set(name1) & set(name2)
print(f"{common_names = }")

# Names appear in only one of the lists
uncommon_names = set(name2).symmetric_difference(set(name1))
print(f"{uncommon_names = }")

# All names in both lists
all_names = set(name1) | set(name2)
print(f"{all_names = }")

#%% Conditional statement
num = int(input("Enter an integer: "))

# Use if-else statement
if num % 2:
    print("This is an odd number.")
else:
    print("This is an even number.")
    
# Use ternary expression
print(f"This is an {'odd' if num % 2 else 'even'} number.")

#%% For loop examples
names = ['ali', 'baba', 'cloud']
ages = [13, 23, 34, 45]
blood_types = ['a', 'o', 'b', 'ab', 'o']

# Use index to loop through multiple lists
for i in range(len(names)):
    print(f"{i+1}. {names[i]} is {ages[i]} years old with blood type {blood_types[i]}.")

# Use zip() to combine multiple lists
for i, j, k in zip(names, ages, blood_types):
    print(f"{i} is {j} years old with blood type {k}.")

# Use enumerate to automatically add an index to each iteration
for h, (i, j, k) in enumerate(zip(names, ages, blood_types), start=1):
    print(f"{h}. {i.capitalize()} is {j} years old with blood type {k.upper()}.")
    
    
#%% While loop example 1
while True:
    num = input("Enter an integer: ")
    if num.isdigit():
        print(f"This is an {'odd' if int(num) % 2 else 'even'} number.")
        break
    else:
        print(f"{num} is not a valid integer!")
    
#%% While loop example 2
while True:
    name = input("Enter your name: ")
    print(f"Hi {name}. Welcome to Python World!")
    ...
    ans = input("Do you want to play again?([y]/n)") or 'y'
    if ans.lower() in ('y', 'yes'):
        continue
    elif ans.lower() in ('n', 'no'):
        print("Good bye and see you soon!")
    else:
        print("Invalid choice! Exiting ...")
    break

#%% List comprehension example 1
# Select the words that start with vowels
words = ('ant', 'boy', 'eggs', 'cake', 'door', 'house', 'owl')

# Method 1 - Use for loop
vowel_words1 = []
for w in words:
    if w[0] in 'aeiou':
        vowel_words1.append(w)
print(f"{vowel_words1 = }")

# Method 2 - Use list comprehension
vowel_words2 = [w for w in words if w[0] in 'aeiou']
print(f"{vowel_words2 = }")

#%% List comprehension example 2
# Calculate the number of odd numbers in a list
from random import randint
numbers = [randint(1, 100) for _ in range(1000)] # insert 100 random numbers between 1 and 100

from time import perf_counter

# Method 1 - Use for loop
start_time = perf_counter()
count = 0
for n in numbers:
    if n % 2:
        count += 1
time_taken1 = perf_counter() - start_time
print(f"There are {count} odd numbers in the list. Time taken: {time_taken1}")


# Method 2 - Use list comprehension
start_time = perf_counter()
count2 = sum([n%2 for n in numbers])
time_taken2 = perf_counter() - start_time
print(f"There are {count2} odd numbers in the list. Time taken: {time_taken2}")

#%% Dictionary comprehension
# Create a new dictionary for discounted price (after 10% discount)
prices = dict(apple=1.5, oranger=2.5, durian=30, mango=12)

# Method 1 - Use for loop
new_prices = {}
for k in prices:
    new_prices[k] = 0.9 * prices[k]
print(f"{new_prices = }")

# Method 2 - Use dictionary comprehension
new_prices2 = {k: 0.9*prices[k] for k in prices}
print(f"{new_prices2 = }")






















