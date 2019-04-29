# Intro_to_python

This code was a part of the Intro to Python workshop by Front End Masters

A small python program that uses the GitHub search API to list the top
projects by languages, based on stars.
Github Search API documentation: https://developer.github.com/v3/search/

# How Python Executes

When we first run our code using CPython, it will compile our python code into python bytecode. Then it will pass the bytecode to Python Virtual Machine which will convert it into machine code.

There are various Python implementations

1. Jython- If you want to write Java code in Java. Here our code will be compiled to java bytecode which the JVM will convert into machine code.

2. PyPy

3. IronPython

# Primitive Types in Python

1. String
2. Numbers- (Int, Float, Complex Numbers)
3. Boolean

New Learnings: String Comparison in Python
Suppose you have str1 as "Mary" and str2 as "Mac" . The first two characters from str1 and str2 ( M and M ) are compared. As they are equal, the second two characters are compared. Because they are also equal, the third two characters ( r and c ) are compared. And because 'r' has greater ASCII value than 'c' , str1 is greater than str2 .

# Return Values from Functions

In Python unlike other programming languages, we can return multiple values.

```python
def increment(number,by):
    return (number,by)


print(increment(2,3))

# Output: (2,3)
```

# Data Structures

# Some Interesting Tit Bits

### Lists

```python
numbers=[1,3,5]
first,second,third=numbers

letters=["a","b","c"]

for letter in enumerate(letters):
    print(letter[0],letter[1])

Output

0 a
1 b
2 c

```

# Lamdas in Python

```python
items=[
("Product1",10),
("Product2",9),
("Product3",12),
]

 items.sort(key=lambda item:item[1])
 print(items)

# The lambda can used in the place of the
  following method

  def sortItems(item):
      return item[1]

   items.sort(key=sortItems)

# Using the Same example from above

items=[
   ("Product1",10),
   ("Product2",9),
   ("Product3",12)
]

# Initial Approach

price=[]

for item in items:
    prices.append(item[1])

print(prices)


# Lambda Approach

x=map(lambda item:item[1],items)

for item in x:
    print(item)

# List comprehensions

prices=[item[1] for item in items]

```

# Generator Expressions

```python

values=(x*2 for x in range(5))
print("list:", getsizeof(values))

print(len(values))

# Output:

gen:120
Error: Object of generator type have no values.


```

# Factory methods in Python

```python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Here cls is a reference to the class Point

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print("draw")


# Python Factory Functions
point = Point.zero()

```
