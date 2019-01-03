
####################
#### commenting ####
####################
spam = 1 # This is a comment
text = "# This is not a comment"


########################
### basic operations ###
########################
print(3/2) # Division returns floating point numbers


####################
##### exponents ####
####################
print(5 ** 2) # Base ** power


####################
##### variables ####
####################
width = 20 # = is used to assign a value to a variable
height = 9
print(width * height)


####################
###### strings #####
####################
string1 = 'spam eggs'
string2 = "spam eggs"
print(string1)
print(string2)


####################
### raw strings ####
####################
print("C:\some\name") # Here, \n acts as a newline character
print(r"C:\some\name") # raw string


############################
### print multiple lines ###
############################
print("""
Usage: thing [options]
    -# HACK:
    -H hostname
""")


####################
#### concatenate ###
####################
print("Be" + 2*"n" + "e" + 2*"t")


###################################
### concatenate string literals ###
###################################
print("Be" "nn" "ett") # String literals next to
                       # each other are concatenated


#######################
### string indexing ###
#######################
word = "Bennett"
print(word[0]) # First character
print(word[-1]) # Last character
print(word[0:3])
print(word[:3])


####################
####### list #######
####################
l = [1, 2, 3]
print(l)


####################
####### while ######
####################
a, b = 0, 1 # Multiple assignment
while a < 10:
    print(a)
    a, b = b, a+b


####################
### if/elif/else ###
####################
x = int(input("Please enter integer: "))
if x < 0:
    x = 0
    print("Negative changed to zero")

elif x == 0:
    print("Zero")

else :
    print("more")


######################
### for statements ###
######################
words = ['cat', 'window', 'defenestrate']
for w in words: # Iterates over items in a sequence (like a list or string)
    print(w, len(w))


################################
### for statement over slice ###
################################
for w in words[1:2]: # iterate only over the slice of the list
                     # (makes a copy of the slice)
    if len(w) > 6:
        words.insert(0,w)


########################
### range() function ###
########################
for i in range(5): # sequence from 0 to 5 by 1
    print(i)

range(5, 10) # sequence from 5 to (less than 10) by 1
range(0, 10, 3) # sequence from 0 to (less than 10) by 3

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(range(10)) # range() does not return a list, it returns an iterable
                 # so printing range(10) shows "range(0, 10)"
                 # functions and constructs that use iterables are iterators
                 # ex. for loops, list()


######################
### break/continue ###
######################
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print (n, "equals", x, "*", n//x) # concatenate adds a space
                                              # between elements
            break #breaks out of the inner most loop
    else: # Loops can have else statements that runs when the for loop
          # goes through entire list
          # or the while loop condition becomes false. It does not
          # run when a break occurs.
        print(n, "is a prime number")

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue # continue continues with the next iteration of the loop
                 # without finishing any code in the current iteration
    print("Found a number", num)


######################
### pass statement ###
######################
def initlog(*args):
    pass # a null statement but allows unimplemented code to compile


####################
##### functions ####
####################
def fib(n): # Define function
    """Print a Fibonacci series up to n""" #docstring
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()

fib(2000) # Call function


#########################
### default arguments ###
#########################
def ask(prompt, retries=4, reminder="please try again"):
    while True:
        ok = input(prompt)
        if ok in ("y", "ye", "yes"): # in keyword test whether sequence
                                    # contains certain value
            return False
ask("Do you want") # Calls function with only one argument. The arguments not
                   # specified will take their default values

i=5
def f(arg=i): # Default value is evaluated at the point of function definition
    print(arg)

i=6 # Does not change default value of function argument
f()

# default arguments can be called positionally or through keywords
# ask("A", 1, "B") 3 positional arguments
# ask (reminder="B", prompt="A", 1) 3 keyword arguments
# Cannot have positional arg after keyword arg


##############################
### alternative parameters ###
##############################
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    for arg in arguments: # *argument accepts a tuple
        print (arg)
    for kw in keywords: # **keywords accepts sa dictionary
        print(kw, ":", keywords[kw])

cheeseshop("Limberger", "It's ver runny", "It's very Very runny",
        shopkeeper="Mike", client="John", sketch="cheese shop")
# The first parameter is for kind
# the next two form a tuple that is for *arguments
# the final three form a dictionary for **keywords

# tuples must come before dictionaries in funcion definitions


###########################
### arbitrary arguments ###
###########################
def write_multiple(file, separator, *args): # *args will scoop up any remaining
                                            # parameters in the function call
    file.write(separator.join(args))


######################
### argument lists ###
######################
list(range(3, 6))
args = [3, 6]
list(range(*args)) # is the same as list(range(3, 6))

def parrot(voltage, state="a stiff", action="voom"):
    pass

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


##########################
### lambda expressions ###
##########################
def make_incrementor(n): # Uses lambda expression to return a function
    return lambda x: x + n # Lambda function is the same as a normal function
                           # definition but more readable and concise

f = make_incrementor(42)
f(0) # 42
f(1) # 43

pairs=[(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1]) # Lambda expression to pass function as arg
                                     # obj.methodname performs function
                                     # "methodname" that belongs to obj
pairs


########################################
### documentation strings (doctring) ###
########################################
def my_function():
    # The first line is the summary.
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    # The latter lines should be one or more paragraphs describing
    # the functions calling conventions, side effects, etc.
    # By default, the non-summary will be indented
    pass

print (my_function.__doc__)


###########################
### function annotation ###
###########################
# Optional metadata about the types in a user-defined function
def a(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", a.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

a("spam")


####################
### coding style ###
####################
# 1. use 4-space indentation
# 2. wrap lines at 80 characters
# 3. use blank lines to separate functions and classes, and large blocks of code
# 4. put comments on their own lines
# 5. use doctrings
# 6. use spaces around operators and after commas
# 7. CamelCase for classes and lower_case_underscore for functions and methods
# 8. always use UTF-8 encoding or plain ASCII
# 9. no non-ASCII characters


###########################
######## more lists #######
###########################

# list.append(x) adds x to the end of list
# list.extend(iterable) extend the list by appending all items from the iterable
# list.insert(i, x) inserts x at position i in the list
# list.remove(x) removes the first item in the list with value equal to x. Gives
#       error if there is no matching item
# list.pop(i) removes and returns the item at position i
# list.pop() removes and returns the last item in the list
# list.clear() removes all items from list. equivalent to del a[:]
# list.index(x[, start[, end]]) returns the index of the first item in list that
#       matches x. start and end are optional and limit the search to a slice
# list.count(x) returns number of times x appears in the list
# list.sort(key=None, reverse=False) sorts the items in list with key being the
#       comparison function
# list.reverse() reverses the elements of the list in place
# list.copy() returns shallow copy of the list. equivalent to a[:]

fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruits.count("apple"))
fruits.count("tangerine")
fruits.index("banana")
fruits.index("banana", 4)
fruits.reverse()
print(fruits)
fruits.append("grape")
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()


#######################
### lists as stacks ###
#######################
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack.pop())


#######################
### lists as queues ###
#######################
# not efficient so we import
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
print(queue.popleft())
print(queue)


############################
### lists comprehensions ###
############################
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
# After the loop is finished, there will still be a global variable x with
#   some value

squares = list(map(lambda x: x**2, range(10)))
# or
squares = [x**2 for x in range(10)] # this is the list comprehension

combs = []
[(x,y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# is equivalent to
combs2 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))


###################################
### nested lists comprehensions ###
###################################
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)

# transpose rows and columns
print([[row[i] for row in matrix] for i in range(4)])


#######################
#### del statement ####
#######################
# removes an item from a list given index and does not return a value
e = [-1, 1, 66.25, 333, 333, 1234.5]
del e[0]
print(e)
del e[2:4]
print(e)
del e[:] # clears entire list
print(e)


############################
### tuples and sequences ###
############################
tuple = 12345, 54321, "hello"
print(tuple[0])
tuple2 = tuple, (1, 2, 3, 4, 5) # nested tuple
print(tuple2)
# tuples are immutable so you cannot do something like tuple[0] = 55555
# they can contain mutable objects like lists though
empty = () # tuple with zero items
single = "first", # tuple with one item
# a tuple, like a list or a string is a sequence


##########################
### sequence unpacking ###
##########################
g, h, j = tuple
print(tuple)
print(g)
print(h)
print(j)


#######################
######### sets ########
#######################
# sets are unordered collections with no duplicates
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket) # duplicates automatically removed
print("orange" in basket)

a = set("abracadabra")
b = set("alacazam")
print(a)
print(b)
print(a - b) # letters in a but not in b
print(a | b) # letters in either a or b or both
print(a & b) # letters in both a and b
print(a ^ b) # letters in a or b but not both (XOR)

a = {x for x in "abracadabra" if x not in "abc"}
print(a)


####################
### dictionaries ###
####################
# set of key/value pairs. keys must be unique and immutable
tel = {"jack": 4098, "sape": 4139}
tel["guido"] = 4127
print(tel)
print(tel["jack"])
del tel["sape"]
print(tel)
print(list(tel)) # prints list of keys
print(sorted(tel))
print("guido" in tel)

# dictionary constructor
key_list = [("sape", 4139), ("guido", 4127), ("jack", 4098)]
new_dict = dict(key_list)
print(new_dict)
{x: x**2 for x in (2, 4, 6)} # Dictionary comprehensions


##########################
### looping techniques ###
##########################
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items(): # .items retrieves key and value at the same time
    print(k, v)

for i, v in enumerate(["tic", "tac", "toe"]): # enumerate retrieves position
                                              # index and value at the same time
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers): # loops over two or more sequences at the
                                     # same time
    print("What is your {0}? It is {1}.".format(q, a))

for i in reversed(range(1, 10, 2)): # loop over sequence in reverse
    print(i)

for i in sorted(set(basket)): # loops over sorted copy of list
    print(i)


##########################
####### comparisons ######
##########################
# "in" and "not in" check whether values are found in a sequence
# "is" and "is not" check if two objects are the same object
# comparisons can be chained (a < b == c) tests whether a is less than b and
#       and b equals c
# boolean operators "and", "or", "not"

# sequences can be compared with sequences of the same type
# sequences are compared by comparing the first two items, if they are the
#       same, then compare the next items
(1, 2, 3) < (1, 2, 4)
[1, 2, 3] < [1, 2, 4]
"ABC" < "ACB"
(1, 2, 3, 4) < (1, 2, 3)
(1, 2, 3) == (1.0, 2.0, 3.0)
(1, 2) < (1, 2, -1)
(1, 2, ("aa", "ab")) < (1, 2, ("abc", "a"), 4)


##########################
######### modules ########
##########################
# A module is a file containing Python definitions
# and statements. You use a module to share things
# between files in a large program without having
# to retype definitions

# I have created fibo.py which contains function
# to print and return a fibonacci sequence

import fibo
print(fibo.fib(1000)) # prints "None" because the function has no return
print(fibo.fib2(100))
print(fibo.__name__)

# Each module has a local symbol table which is used as a global symbol
# table for all functions defined in the module

# Can access a modules global variables with module.itemname

# Modules can import other modules
from fibo import fib
fib(500)
# fib2 not defined here

from fibo import * # imports all names that a module defines

import fibo as fib
fib.fib(500)

# Each module is only imported once per interpretter session so
# to change your modules, you must restart interpretter
# to test a single module change
# import importlib
# importlib.reload(modulename)


##########################
### modules as scripts ###
##########################
# Run a python module from command line with
# python3 module.py <arguments>

# For a module to be run as a script, add the following to the
# end of the module

# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))

# these lines will be run if the module is not imported

# python comes with library of standard modules


##########################
########## dir() #########
##########################
# dir(module_name) returns a sorted list of names a module defines
# dir() lists names defined currently


##########################
######## packages ########
##########################
# A package is a container for a set of modules
# A package can contain subpackages
# "import package.subpackage.module"

# from package.subpackage import * imports all the modules defined
# in a list named __all__ within the subpackages __init__.py
# If __all__ is not defined, it only ensures that the package sound.effects
# has been imported, cannot guarantee that all submodules are imported

# from . import module (imports module from current package)
# from .. import module (imports module from parent package)


#########################
### output formatting ###
#########################
year = 2016
event = "Referendum"
print(f"results of the {year} {event}") # formatted string literal

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print("{:-10} YES votes {:10.4%}".format(yes_votes, percentage))
# {index within .format(): indentation.decimals}


#################################
### reading and writing files ###
#################################
# open() returns a file object
file = open("practice_file", "w") # can be "w" write, "r" read (default)
                                  # or "r+" for read and write
file.close()

with open("practice_file") as f: # This syntax automatically closes the file
    read_data = f.read()
f.closed

# f.read(size)
# f.readline() reads single line until newline character
# f.write()
# f.seek(offset, from_what) from_what 0 is beginning of file, 1 is current
#                           location, 2 is end of file
# f.tell() returns integer giving the file object's current position


########################
######### JSON #########
########################
# view json string representation of object x
import json
x = [1, "simple", "list"]
print(json.dumps(x))

file = open("practice_file", "w")
json.dump(x, file)
file.close()

file = open("practice_file", "r")
y = json.load(file)
file.close()


#############################
### errors and exceptions ###
#############################
# a syntactically incorrect statement will not allow the program to compile
# and is called an error

# a syntactically correct statement that will cause errors during execution
# is called an exception


##########################
### exception handling ###
##########################
while True:
    try: # try clause
        x = int(input("Please enter a number: "))
        break
    except ValueError: # if exception occurs within the try clause, the rest of
                       # the try is skipped and except clause is executed
        print("That is not a valid number")

# a try can have more than one except
# an except can name more than one exception "except (RuntimeError, TypeError)"
# else clause after except will run if no exception is raised

# the raise statment allows programmer to force a specific exception to occur


###############################
### user-defined exceptions ###
###############################
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


#########################
######## finally ########
#########################
# a finally clasue is executed before leaving the try statement, regardless
# of whether an exception has occurred or not.
# try:
#     raise KeyboardInterrupt
# finally:
#     print("Goodbye, World!")


#########################
######### scopes ########
#########################
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local asignment:", spam) # will print test spam because we are
                                          # not within the container of the
                                          # local assignment
    do_nonlocal()
    print("After nonlocal assignment:", spam) # will print nonlocal spam
    do_global()
    print("After global assignment:", spam) # will print nonlocal spam because
                                            # we are still within the container
                                            # immediately outside the assignment

scope_test()
print("In global scope:", spam) # will print global spam


#########################
### class definitions ###
#########################
class ClassName:
    """A simple example class.

    It includes data attributes and methods"""

    i = 12345

    def f(self):
        return "hello world"

#ClassName.i returns an integer
#ClassName.f returns a function object

x = ClassName() # object instantiation

# instantiating an a class creates an empty object
# if the class has __init__() method, the object may be initialized
# with specific values

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)


####################################
### class and instance variables ###
####################################
class Dog:
    kind = "canine" # class variable shared by all instances

    def __init__(self, name):
        self.name=name # instance variable unique to each instance

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x) # self keyword refers the the enclosing object

    def addtwice(self, x):
        self.add(x)
        self.add(x)

# an objects class is stored as "object.__class__"


###################
### inheritance ###
###################
class BaseClassName():
    pass

class DerivedClassName(BaseClassName): # or "modulename.BaseClassName"
    pass
    # <statement-1>
    # .
    # .
    # .
    # <statement-N>

# use isinstance() to check an instance's type: "isinstance(obj, int)" is true
# only if obj.__class__ is int or a class derived from int

# use issubclass() to check class inheritance: "issubclass(bool, int)" is True
# since bool is a subclass of int

class Base1():
    pass
class Base2():
    pass
class Base3():
    pass
class DerivedClassName(Base1, Base2, Base3): # multiple inheritance
    pass

# if an attribute is not found in DerivedClassName, it is
# searched for in Base1, then Base2, and so on.


#########################
### private variables ###
#########################
# private variables that cannot be accessed except from inside an object do
# not exist in python.

# by convention, variables that are prefixed with an underscore (_spam) are
# considered non-public part of the API and are merely an implementation detail
# subject to change

# there is a limited support for class-private members. __spam is textually
# replaced with _classname__spam where classname is the current class name
# this is just a technique to avoid accidents not required


####################################
### bundling together data items ###
####################################
# using an empty class, we can bundle data items
class Employee:
    pass

john = Employee() # john is a bundle of data items now

john.name = "John Doe"
john.dept = "computer lab"
john.salary = 1000

# code that expects a particular ADT can be passed a class that looks like that
# ADT


#########################
####### iterators #######
#########################
# a for loop calls iter() on a container object and returns an iterator object.
# the iterator objects method __next__() accesses elements in the container one
# at a time. We can call __next__() with the next() function
s = "abc"
it = iter(s)
print(it)
print(next(it))
next(it)
next(it)
# print(next(it)) # will raise exception because we are beyond the range of
                # our container object

# within a class of our own, we can define __iter__() and __next__() methods
class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


##########################
####### generators #######
##########################
# a tool to create iterators. when next() is called, the generator
# resumes the data values and which statement was last executed.
def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index] # yield statement returns data
# a generator creates __iter__() and __next__() automatically so
# they can be written compactly


#############################
### generator expressions ###
#############################
# like list comprehensions but for simple generators
sum(i*i for i in range(10))
data = "Bennett"
list(data[i] for i in range(len(data) - 1, -1, -1))


########################
### standard library ###
########################
# os
# interact with the operating system
import os
os.getcwd() # returns the current working directory
# os.chdir(new_dir) changes the working directory
# os.system(command) runs the command in the system shell
help(os) # help() returns a manual from the module's doctrings

# shutil
# provides higher lever interfce for file and directory management tasks
# import shutil
# shutil.copyfile("data.db", "archive.db")
# shutil.move("/buiild/executables", "installdir")

# glob
import glob
glob.glob("*.py") # makes a file list from directory wildcard searches

# sys
# stores system items
import sys
print(sys.argv) # prints command line arguments for scripts

# re
# regex string processing
# includes regular expressions
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# and string methods for simpler needs
'tea for too'.replace('too', 'two')

# math
# access to the C library functions for floating point math
import math
math.cos(math.pi / 4)

# random
# tools for random selection
import random
random.choice(["apple", "pear", "banana"])
random.sample(range(100), 10)

# statistics
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
statistics.median(data)
statistics.variance(data)

# urllib.request
# retrieve data from URLs
# from urllib.request import urlopen
# with urlopen("http://tycho.usno.navy.mil/cgi-bin/timer.p1") as response:
#     for line in response:
#         line = line.decode("utf-8")
#         if "EST" in line or "EDT" in line:
#             print(line)

# datetime
# manipulating dates and times
from datetime import date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = date(1997, 7, 31)
age = now - birthday
print(age.days)

# zlib, gzip, bz2, lzma, zipfile, tarfile
# data archiving and compression
import zlib
s = b'witch which has wich witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))

# timeit, profile, pstats
# performance measuring
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

# doctest
# scanning a module and validating tests embedded in a program's doctrings
import doctest
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """

    return sum(values) / len(values)

print(doctest.testmod())

# unittest
# a more comprehensive set of tests maintained in separate file
import unittest
class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

print(unittest.main()) # invokes all tests
