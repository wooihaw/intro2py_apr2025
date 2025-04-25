# In-class examples for Day 3
#%% Exception handling
while True:
    try:
        num = int(input("Enter an integer: "))
    except ValueError as e:
        print(f"Error: {e}")
    else:
        break
print(f"You have enter {num}")

#%% Function and return value
def fun1(x, y):
    print(x + y)
    
def fun2(x: int|float, y: int|float) -> int|float:
    '''This is a function to add 2 arguments.
    written by ABC'''
    return x + y

a = fun1(12, 34)
b = fun2(56, 78)

print(f"{a = }, {b = }")

#%% Function to return multiple values
def fun3(x: int|float, y:int|float, z:int|float) -> int|float:
    '''This is a function which returns 3 values'''
    return 2*x, 3*y, 4*z

c = fun3(3, 5, 7)
print(f"{c = }")

d, e, f = fun3(2, 4, 6)
print(f"{d = }, {e = }, {f = }")

#%% Functions are objects
def funA(x: int|float) -> int|float:
    return x + 1

def funB(y: int|float) -> int|float:
    return y * 2

def funC(z: int|float) -> int|float:
    return z - 3

all_func = (funA, funB, funC)
alist = [4, 5, 6, 7]

for i in alist:
    for f in all_func:
        print(f"{f}: {f(i)}")

#%% Anonymoous function example 1
alist = [(1, 2, 3), (11, 4, 1), (7, 9, 2)]
blist = sorted(alist)
print(f"{alist = }, {blist = }")

# To sort according to the 3rd element of each tuple in descending order
clist = sorted(alist, key=lambda x:-x[2])
print(f"{clist = }")

#%% Anonymous function example 2
# Sort the list based on the numbers in the IDs
IDs = ['ID21', 'ID7', 'ID55', 'ID101', 'ID3', 'ID83', 'ID11', 'ID234', 'ID57']
sorted_IDs = sorted(IDs)
print(f"{sorted_IDs}")

new_sorted_IDs = sorted(IDs, key=lambda x:int(x[2:]))
print(f"{new_sorted_IDs}")

#%% Anonymous function example 3
alist = ['A', 'quick', 'blue', 'fox']
print(f"{sorted(alist) =}")

# To sort according to the number of alphabets in the words
print(f"{sorted(alist, key=lambda x:len(x)) =}")

blist = ['egg', 'babies', 'ai']
print(f"{max(blist) =}")
print(f"{max(blist, key=lambda x:len(x)) =}")

#%% Example of map() function
# Reverse each string in a list
words = ['apple', 'bell', 'cat', 'door', 'eggs']

# Method 1 - for loop
r1 = []
for w in words:
    r1.append(w[::-1])
print(f"{r1 = }")

# Method 2 - list comprehension
r2 = [w[::-1] for w in words]
print(f"{r2 = }")

# Method 3 - Use map()
r3 = list(map(lambda w:w[::-1], words))
print(f"{r3 = }")

#%% Example of filter() function
#Select only the words which are palindrome
words = ['ant', 'boy', 'dad', 'fish', 'civic', 'mom', 'lady', 'madam']

# Method 1 - for loop
p1 = []
for w in words:
    if w == w[::-1]:
        p1.append(w)
print(f"{p1 = }")

# Method 2 - list comprehension
p2 = [w for w in words if w == w[::-1]]
print(f"{p2 = }")

# Method 3 - Use filter()
p3 = list(filter(lambda w: w==w[::-1], words))
print(f"{p3 = }")

#%% OOP example
class Rectangle:
    desc = "This is a rectangle"
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __str__(self):
        return f"A {self.length} x {self.width} rectangle"
    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"
    def __eq__(self, other):
        return self.area() == other.area()
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*self.length + 2*self.width
    
r1 = Rectangle(2, 3)
r2 = Rectangle(3, 2)
r3 = Rectangle(4, 5)

print(r1)
print(f"{r1 = }, {r1.area()}, {r1.perimeter()}")

if r1 == r2:
    print("They are equal size")
else:
    print("They are not equal size")

# Child class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    def __str__(self):
        return f"A {self.length} x {self.length} square"

s1 = Square(3)
print(s1)
print(f"{s1 = }, {s1.area()}, {s1.perimeter()}")


















