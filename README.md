# Intro_to_python
This code was a part of the Intro to Python workshop by Front End Masters


  A small python program that uses the GitHub search API to list the top
  projects by languages, based on stars.
  Github Search API documentation: https://developer.github.com/v3/search/
  
#  Helpful Python commands

Windows Powershell-> To activate your virtual environment
```
env\scripts\activate

```

Keyboard shortcuts: Ctrl+shift+P
Ctrl + P

# Why do we use Virtual Environments?
  It is extremely useful while working with third party libraries.

```
  type()
  dir()
  help()-Pass in the type
```

# Anatomy of a Python Function

```
	def foo():
		.....print("Hello")
```
>>>foo();
>>>Hello World

# Where dynamic types meeting smart naming conventions

== equality in python
  is, Do the point to the same thing in memory

# Everything is a object in Python
  
  ```
  type([])
  <class 'list'>

  >>> name=["Nina","Max","Rose"]
  >>> len(names)
  >>> 3

```

 dir() is an handy method to know the number of methods available to that
 data type

# Tuples
  Tuples are immutable

For example:
 ```
 x=(1,2,3)

 x[1]=2;
>>> Type Error. Values cannot be re-assigned
```

# Sets
```
  set()
  {1}
  type({1})
  <class 'set'>


  names={"Gidi", "Ronj","Joel"}
  type(names)
>>>Set
```
# hash("Gidi")
  07012709831993

# You can only put immutable items in the set
# Adding and Removing from sets
```
 colors={"Red","Green","Blue"}
 colors.add("Pink")

 colors.discard("Green")
 colors.remove("Green")

```

# Sets do not support indexing
# The update method for sets expects a sequence
# Set operations   
```
set1.union(set2)  or  set1 | set2 
set1.intersection(set2) or set & set2
```
  
# The Difference
  
  set1 ^ set2
  Elements that are in set1 but not in set2

  help(set) or dir(set)

# Set is immmutable and the items aren't ordered

# Dictionaries

  Allows us to store data in key value pairs. Dictionary keys are mutable
  Checking to see if key is in a dictionary is a very fast operation
  
  key:value pairs
  ```
  example: nums={ "one": "Gideon", "two":"Aaron". "three":"Stanislaus"}
           nums.get("one", "defaultValue")
  ```

# Dictionaries are ordered in insertion order

  .values()
  .keys()
  .items()



# equality == !=
  identity is keyword


# In JavaScript, arrays and objects are passed by reference
  while variables are passed by values


# and , or , not
  
  ```
  a=True
  b=True
  
  a and b
  >>true
  If the value of a is true then it prints the value of b
 
 ```
# Ctrl + Shift + P
  Run Python file in the terminal

# python file_name.py     //Running it outside of Visual Code

# If the code needs to be reusable , we need to put it in the main method



