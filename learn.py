####################################################
## 0. Useful stuff about Python
####################################################
# Pyhton Enhancement Proposals, or PEPs, are useful conventions which guide
# the user in writing readable and pretty code, as well as many other
# details about Python. PEP-8 is the Style Guide (https://www.python.org/dev/peps/pep-0008/)

# According to PEP-8, line length should be limited to 79 characters

# No brackets are used for code blocks. Instead, indentation is used
# The general consensus is to use 4 spaces, but it is not necessary
# What is necessary is to NOT mix tabs and spaces. Python will complain
# NOTE: You can still press the "Tab" key, but make sure your IDE is set
# up so that it will type 4 spaces per press.

# snake_case is the norm, as opposed to camelCase as is standard in other
# languages

# Single line comments start with a hash symbol.

""" Multiline strings can be written
    using three "s, and are often used
    as documentation (docstrings).
"""

type(a_variable)    # Used to find out the type of a variable
help(an_object) # Used to print documentation about a class or function (the
                # ones written in the triple double-quotes)
dir(an_object)  # Used to find all the variable and function names of
                # an object or module
            
# Special Python variables will be surrounded by double underscores.
# A particularly useful one is __name__, which lets the module know 
# if it is the one being executed as the main program, in which case that
# module's __name__ = "__main__", otherwise it will be its own filename.
# https://www.geeksforgeeks.org/__name__-special-variable-python/

# EVERYTHING in Python is an object

# Python has a print function. We'll look at functions later, for now:
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you!

# By default the print function also prints out a newline at the end.
# Use the optional argument end to change the end string.
print("Hello, World", end="!")  # => Hello, World!

# Simple way to get user input data from console
input_string_var = input("Enter some data: ") # Returns the data as a string
# Note: In earlier versions of Python, input() method was named as raw_input()

####################################################
## 1. Primitive Datatypes and Operators
####################################################

# Math is what you would expect
1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20
35 / 5  # => 7.0

# Integer division rounds down for both positive and negative numbers.
5 // 3       # => 1
-5 // 3      # => -2
5.0 // 3.0   # => 1.0 # works on floats too
-5.0 // 3.0  # => -2.0

# The result of division is always a float
10.0 / 3  # => 3.3333333333333335

# Modulo operation
7 % 3  # => 1

# Exponentiation (x**y, x to the yth power)
2**3  # => 8

# Enforce precedence with parentheses
1 + 3 * 2  # => 7
(1 + 3) * 2  # => 8

# Round numbers manually with round()
round(5.5) # => 6
round(5.758, 2) # => 5.76

# Work in other bases (binary, octal and hexadecimal)
0b10 # => 2
0o10 # => 8
0x10 # => 16

# Scientific notation is also accepted
2.99e8
1.65e-30

# Using underscores, you can make large numbers more legible
10000000 == 10_000_000 # => True

# Boolean values are primitives (Note: the capitalization)
True  # => True
False  # => False

# negate with not
not True   # => False
not False  # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False  # => False
False or True   # => True

# True and False are actually 1 and 0 but with different keywords
True + True  # => 2
True * 8    # => 8
False - 5   # => -5

# Comparison operators look at the numerical value of True and False
0 == False  # => True
1 == True   # => True
2 == True   # => False
-5 != False  # => True

# Using boolean logical operators on ints casts them to booleans for evaluation, but their non-cast value is returned
# Don't mix up with bool(ints) and bitwise and/or (&,|)
bool(0)     # => False
bool(0.0)   # => False
bool(4)     # => True
bool(-6)    # => True
0 and 2     # => 0
-5 or 0     # => -5

# Equality is ==
1 == 1  # => True
2 == 1  # => False

# Inequality is !=
1 != 1  # => False
2 != 1  # => True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Seeing whether a value is in a range
1 < 2 and 2 < 3  # => True
2 < 3 and 3 < 2  # => False
# Chaining makes this look nicer
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # => True, a and b refer to the same object
b == a            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal

# Strings are created with " or '. There is no 'char' type unlike in other languages
"This is a string."
'This is also a string.'

# Strings can be added too! But try not to do this.
"Hello " + "world!"  # => "Hello world!"
# String literals (but not variables) can be concatenated without using '+'
"Hello " "world!"    # => "Hello world!"

# A string can be treated like a list of characters
"Hello world!"[0]  # => 'H'

# You can find the length of a string
len("This is a string")  # => 16

# You can split strings based on a delimiter, by default, space
"This string".split()

# You can also format using f-strings or formatted string literals (in Python 3.6+)
name = "Reiko"
f"She said her name is {name}." # => "She said her name is Reiko"
# You can basically put any Python statement inside the braces and it will be output in the string.
f"{name} is {len(name)} characters long." # => "Reiko is 5 characters long."
number = 250_000_000
f"{number:,}" # => 100,000,000

# And raw strings too
path = r"C:\Users\Documents" # => Prints it as is

# Bytes are a thing, usually used when working with raw binary data
data = b"some binaty data"
# Python allows encoding and decoding of said data into strings and viceversa
string_1 = "Hey, thís is ä string with Ùnicode charactêrs"
bytes_1 = string_1.encode("utf-8") # => b'Hey, th\xc3\xads is \xc3\xa4 string with \xc3\x99nicode charact\xc3\xaars'
bytes_1.decode("utf-8") # => Hey, thís is ä string with Ùnicode charactêrs


# 'None' is an object too
None  # => None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality of object identity.
"etc" is None  # => False
None is None   # => True

# None, 0, and empty strings/lists/dicts/tuples all evaluate to False.
# All other values are True
bool(0)   # => False
bool("")  # => False
bool("False")   # => True
bool([])  # => False
bool({})  # => False
bool(())  # => False

# Casting is available through constructors
int(-2.5) # => -2
int("340")
float(2)
float("2467")
str(450)

# And you can even get infinity
float("inf")
float("-inf")

####################################################
## 2. Variables and Collections
####################################################

# There are no declarations, only assignments. A new object is created
# on every assignment, but x = 300, x = 5, x = 300 will have created 2
# separate int objects. Technically, variables in Python are actually
# references to objects
some_var = 5
some_var  # => 5

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
some_unknown_var  # Raises a NameError

# if can be used as an expression
# Equivalent of C's '?:' ternary operator
"yahoo!" if 3 > 2 else 2  # => "yahoo!"
# Un-pythonic alternative, usually best to avoid it
(value_if_false, value_if_true)[test]

# Lists store sequences
li = []
# You can start with a prefilled list
other_li = [4, 5, 6]

# Add stuff to the end of a list with extend
li.extend("a", "b")  # li is now ["a", "b"]
li = []

# Add 1 element to the end with append
li.append(1)    # li is now [1]
li.append(2)    # li is now [1, 2]
li.append(4)    # li is now [1, 2, 4]
li.append(3)    # li is now [1, 2, 4, 3]
li.append((5, 6))  # li is now [1, 2, 4, 3, (5, 6)]

# Remove from the end with pop
li.pop()        # => (5,6) and li is now [1, 2, 4, 3]
li.pop()        # => 3 and li is now [1, 2, 4]
# Let's put it back
li.append(3)    # li is now [1, 2, 4, 3] again.

# Access a list like you would any array
li[0]   # => 1
# Look at the last element
li[-1]  # => 3

# Looking out of bounds is an IndexError
li[4]  # Raises an IndexError

# Slicing
# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
li[1:3]   # Return list from index 1 to 3 => [2, 4]
li[2:]    # Return list starting from index 2 => [4, 3]
li[:3]    # Return list from beginning until index 3  => [1, 2, 4]
li[::2]   # Return list selecting every second entry => [1, 4]
li[::-1]  # Return list in reverse order => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]

# Make a one-layer-deep shallow copy using slices
li2 = li[:]  # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.

# Other ways to copy lists are:
li2 = list(li)  # This tends to be the best option, since it will work almost
                # always regardless of li's type
li2 = li.copy() # Only works if li is a list

# CAREFUL: if a list contains mutable objects, modifying them in li2 would
# still change them in li, even though they are different lists. For example:
li1 = [[1,2], [3,4]]
li2 = li1[:] # list(li1) or li1.copy() would also work

li2 is li1 # False
li2 == li1 # True
li2[0] is li1[0] # True

# Remove arbitrary elements by index from a list with "del"
del li[2]  # li is now [1, 2, 3]

# Remove first occurrence of a value
li.remove(2)  # li is now [1, 3]
li.remove(2)  # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
li.insert(1, 2)  # li is now [1, 2, 3] again

# Get the index of the first item found matching the argument
li.index(2)  # => 1
li.index(4)  # Raises a ValueError as 4 is not in the list

# You can add lists
# Note: values for li and for other_li are not modified.
li + other_li  # => [1, 2, 3, 4, 5, 6]

# Concatenate lists with "extend()"
li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]

# Check for existence in a list with "in"
1 in li  # => True

# Examine the length with "len()"
len(li)  # => 6

# Reverse and sort lists
li.reverse() # [6, 5, 4, 3, 2, 1]
li.sort() # [1, 2, 3, 4, 5, 6]

# reversed and sorted are used to not modify the original list, but return
# a new one
print(sorted(li)) # returns new list
print(reversed(li)) # returns new iterator, not list

# Generally, you want to use sorted() since it can work with immutable objects
# and won't mess up the original

# Choose a random element of any collection
import random
random.choice(iterable)

# Tuples are like lists but are immutable.
tup = (1, 2, 3)
tup[0]      # => 1
tup[0] = 3  # Raises a TypeError

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

# You can do most of the list operations on tuples too
len(tup)         # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]          # => (1, 2)
2 in tup         # => True

# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6  # tuple 4, 5, 6 is unpacked into variables d, e and f
# respectively such that d = 4, e = 5 and f = 6
# Now look how easy it is to swap two values
e, d = d, e  # d is now 5 and e is now 4


# Dictionaries store mappings from keys to values
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# Immutable types include ints, floats, strings, tuples.
invalid_dict = {[1,2,3]: "123"}  # => Raises a TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}   # Values can be of any type, however.

# Look up values with []
filled_dict["one"]  # => 1

# Get all keys as an iterable with "keys()". We need to wrap the call in list()
# to turn it into a list. We'll talk about those later.  Note - for Python
# versions <3.7, dictionary key ordering is not guaranteed. Your results might
# not match the example below exactly. However, as of Python 3.7, dictionary
# items maintain the order at which they are inserted into the dictionary.
list(filled_dict.keys())  # => ["three", "two", "one"] in Python <3.7
list(filled_dict.keys())  # => ["one", "two", "three"] in Python 3.7+


# Get all values as an iterable with "values()". Once again we need to wrap it
# in list() to get it out of the iterable. Note - Same as above regarding key
# ordering.
list(filled_dict.values())  # => [3, 2, 1]  in Python <3.7
list(filled_dict.values())  # => [1, 2, 3] in Python 3.7+

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict  # => True
1 in filled_dict      # => False

# Looking up a non-existing key is a KeyError
filled_dict["four"]  # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None
# The get method supports a default argument when the value is missing
filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)  # => 4

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5

# Adding to a dictionary (updates value if key already existed)
filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # another way to add to dict

# Remove keys from a dictionary with del
del filled_dict["one"]  # Removes the key "one" from filled dict

# From Python 3.5 you can also use the additional unpacking options
{'a': 1, **{'b': 2}}  # => {'a': 1, 'b': 2}
{'a': 1, **{'a': 2}}  # => {'a': 2}


# Sets store ... well sets
empty_set = set()
# Initialize a set with a bunch of values. Yeah, it looks a bit like a dict. Sorry.
some_set = {1, 1, 2, 2, 3, 4}  # some_set is now {1, 2, 3, 4}

# Similar to keys of a dictionary, elements of a set have to be immutable.
invalid_set = {[1], 1}  # => Raises a TypeError: unhashable type: 'list'
valid_set = {(1,), 1}

# Add one more item to the set
filled_set = some_set
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
# Sets do not have duplicate elements
filled_set.add(5)  # it remains as before {1, 2, 3, 4, 5}

# Remove one or more items with remove or discard
filled_set.remove(6) # Raises KeyError since there's no 6
filled_set.discard(6) # Is silent

# NOTE: Set operations can also be performed with functions, not shown here
# Do set intersection with &  
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# Do set union with |
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# Do set difference with -
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}

# Do set symmetric difference with ^
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}

# Check if set on the left is a superset of set on the right
{1, 2} >= {1, 2, 3} # => False

# Check if set on the left is a subset of set on the right
{1, 2} <= {1, 2, 3} # => True

# Check for existence in a set with in
2 in filled_set   # => True
10 in filled_set  # => False

# Make a one layer deep copy
filled_set = some_set.copy()  # filled_set is {1, 2, 3, 4, 5}
filled_set is some_set        # => False


####################################################
## 3. Control Flow and Iterables
####################################################

# Let's just make a variable
some_var = 5

# Here is an if statement. Indentation is significant in Python!
# Convention is to use four spaces, not tabs.
# This prints "some_var is smaller than 10"
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:    # This elif clause is optional.
    print("some_var is smaller than 10.")
else:                  # This is optional too.
    print("some_var is indeed 10.")


"""
For loops iterate over lists
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))

"""
"range(number)" returns an iterable of numbers
from zero to the given number
prints:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(lower, upper)" returns an iterable of numbers
from the lower number to the upper number
prints:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)

"""
"range(lower, upper, step)" returns an iterable of numbers
from the lower number to the upper number, while incrementing
by step. If step is not indicated, the default value is 1.
prints:
    4
    6
"""
for i in range(4, 8, 2):
    print(i)

"""
To loop over a list, and retrieve both the index and the value of each item in the list
prints:
    0 dog
    1 cat
    2 mouse
"""
animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)

"""
To loop over a dictionary, you can use the for ... in ... with the dictionary
itself, which iterates over the keys, as well as .items() for key value tuples
or .values() to only get the values:
"""
sample_dictionary = {1: "one", 2: "two"}
for key in sample_dictionary:
    print(key)
for key, value in sample_dictionary.items():
    print(key, value)
"""
While loops go until a condition is no longer met.
prints:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x + 1

# Exception Handling
""" Common errors are:
    IndexError: Index out of range
    ValueError: Object is of the right type, but contains an inappropriate
                value, eg. int("asdasd")
    KeyError: Look-up in a mapping fails. No such key is present
    TypeError: The type is not the expected. Usually not checked for; if your
                code works for more types than expected, it is seen as good
                in Python. If it fails, the exception will be raised anyways
"""
# EAFP (Easier to Ask for Forgiveness than Permission) is deeply ingrained in
# Python. Do not check for specific error codes, but rather for exceptions,
# and avoid preemptive checks, as that would be "asking for permission"

# Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass                 # Multiple exceptions can be handled together, if required.
else:                    # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 #  Execute under all circumstances
    print("We can clean up resources here")

# Instead of try/finally to cleanup resources you can use a with statement
with open("myfile.txt") as f:
    for line in f:
        print(line)

# Writing to a file
contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w+") as file:
    file.write(str(contents))        # writes a string to a file

with open("myfile2.txt", "w+") as file:
    file.write(json.dumps(contents)) # writes an object to a file

# Reading from a file
with open('myfile1.txt', "r+") as file:
    contents = file.read()           # reads a string from a file
print(contents)
# print: {"aa": 12, "bb": 21}

with open('myfile2.txt', "r+") as file:
    contents = json.load(file)       # reads a json object from a file
print(contents)     
# print: {"aa": 12, "bb": 21}


# Python offers a fundamental abstraction called the Iterable.
# An iterable is an object that can be treated as a sequence.
# The object returned by the range function, is an iterable.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)  # => dict_keys(['one', 'two', 'three']). This is an object that implements our Iterable interface.

# We can loop over it.
for i in our_iterable:
    print(i)  # Prints one, two, three

# However we cannot address elements by index.
our_iterable[1]  # Raises a TypeError

# An iterable is an object that knows how to create an iterator.
our_iterator = iter(our_iterable)

# Our iterator is an object that can remember the state as we traverse through it.
# We get the next object with "next()".
next(our_iterator)  # => "one"

# It maintains state as we iterate.
next(our_iterator)  # => "two"
next(our_iterator)  # => "three"

# After the iterator has returned all of its data, it raises a StopIteration exception
next(our_iterator)  # Raises StopIteration

# We can also loop over it, in fact, "for" does this implicitly!
our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i)  # Prints one, two, three

# You can grab all the elements of an iterable or iterator by calling list() on it.
list(our_iterable)  # => Returns ["one", "two", "three"]
list(our_iterator)  # => Returns [] because state is saved


####################################################
## 4. Functions
####################################################

# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement

# A function can be stopped prematurely with return, in which case None will
# be returned instead
def premature_stop_square(x):
    if(type(x) != "int"):
        return
    return x*x

# Calling functions with parameters
add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11

# Another way to call functions is with keyword arguments
add(y=6, x=5)  # Keyword arguments can arrive in any order.

# Function Scope
x = 5

def set_x(num):
    # Local var x not the same as global variable x
    x = num    # => 43
    print(x)   # => 43

def set_global_x(num):
    global x
    print(x)   # => 5
    x = num    # global var x is now set to 6
    print(x)   # => 6

set_x(43)
set_global_x(6)

# Arguments can also have default values, making them optional. These default
# expressions are only evaluated once, meaning a = 5 and b= 5 will occur only
# the first time the function is called. Any other time they won't happen 
def operation_with_defaults(a=5, b=4):
    print(a+b)

operation_with_defaults(2) # => 6

# Always use immutable objects, such as ints or strings, for default values
# or None, if you want to use mutable ones, such as Lists, for the reason
# mentioned above
def add_to_list(list=[]):  # Do not do this
    list.append("a")
    print(list)

add_to_list()  # [a]
add_to_list()  # [a, a]
add_to_list()  # [a, a, a]


def add_to_list_correct(list=None):  # Do this instead
    if list is None:
        list = []
    list.append("a")
    print(list)


# You can define functions that take an indefinite number of
# positional arguments
def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1, 2, 3)

# You can define functions that take an indefinite number of
# keyword arguments, as well
def keyword_args(**kwargs):
    return kwargs

# Let's call it to see what happens
keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}


# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# When calling functions, you can do the opposite of args/kwargs!
# Use * to expand tuples and use ** to expand kwargs.
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)            # equivalent to all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)         # equivalent to all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)  # equivalent to all_the_args(1, 2, 3, 4, a=3, b=4)

# Returning multiple values (with tuple assignments)
def swap(x, y):
    return y, x  # Return multiple values as a tuple without the parenthesis.
                 # (Note: parenthesis have been excluded but can be included)

x = 1
y = 2
x, y = swap(x, y)     # => x = 2, y = 1
# (x, y) = swap(x,y)  # Again parenthesis have been excluded but can be included.


# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13

# There are also anonymous functions
(lambda x: x > 2)(3)                  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

# There are built-in higher order functions
list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]

# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list which can itself be a nested list
[add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# You can construct set and dict comprehensions as well.
{x for x in 'abcddeef' if x not in 'abc'}  # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
{value: key for key, value in some_dict} # This would "reverse" some_dict,
# but keys could be overwritten since values are not unique within a dict 


####################################################
## 5. Modules and Virtual Environments
####################################################

# You can import modules
import math
print(math.sqrt(16))  # => 4.0

# You can get specific functions from a module
from math import ceil, floor
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0

# You can import all functions from a module.
# Warning: this is not recommended
from math import *

# You can shorten module names
import math as m
math.sqrt(16) == m.sqrt(16)  # => True

# And even import specific functions with aliases
from math import sqrt as alias_for_sqrt

# Python modules are just ordinary Python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.

# You can find out which functions and attributes
# are defined in a module.
import math
dir(math)

# If you have a Python script named math.py in the same
# folder as your current script, the file math.py will
# be loaded instead of the built-in Python module.
# This happens because the local folder has priority
# over Python's built-in libraries.

# NOTE: Virtual environments are incredibly useful and highly recommended
# to keep your projects' dependencies unrelated to each other, thus avoiding
# potential conflicts. To set them up, use the 'venv' tool included in Python
# or virtualenv installed through pip. We'll use venv.

# On Windows (either PowerShell or cmd work):
# Ensure pip is up-to-date (comes with Python >=3.4):
python -m pip install --upgrade pip
# Then move to the desired folder and create the virtual env.
cd path/to/your/directory
python -m venv <MyEnv> #Change <MyEnv> for the name you want

# And activate the environment
<MyEnv>\Scripts\activate.bat # on cmd
<MyEnv>\Scripts\Activate.ps1 # on PowerShell
        # NOTE: you might get an error on PS. Fix it by running
        # Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# This should now put you inside the virtual environment
# Again, ensure pip is up to date and start installing modules!
python -m pip install -U pip # 'python -m easy_install pip' or '<MyEnv>\Scripts\easy_install-3.8.exe -U pip' if it doesn't work

pip install modulename

# And exit the virtual environment when done
deactivate

####################################################
## 5.1 Pandas
####################################################
# Pandas is a module made for data analysis and manipulation. It offers
# data structures and operations for manipulating numerical tables and time series.

# https://pandas.pydata.org/

# Pandas works with DataFrames, comprised of rows and columns
# and Series, successions of values (equivalent to 1 column)

# Commonly imported with
import pandas as pd
# Changing and resetting options
pd.options.display.max_rows = 30
pd.reset_option("max_rows")

my_series = pd.Series([1,2,3])
# DFs can be created from dictionaries
my_df = pd.DataFrame({
    "Column1": ["Row1", "Row2", "Row3", "Row4"],
    "Column2": my_series
}) #Row4 will have NA/NaN value since my_series only has 3 values

# Read from/Write to csv
df = pd.read_csv("/somedirectory/csv")
df.to_csv("name of the csv file.csv")

# Read from/Write to Excel
df2 = pd.read_excel("/somedirectory/excel")
df2.to_xlsx("name of the excel file.xlsx")

# Adding new columns
my_df['Column3'] = [some_value, some_other_value]

# Simple way to write a new column derived from others
my_df["Column7"] = [int(row[1]["Column1"] and row[1]["Column2"]) for row in my_df.iterrows()]

# describe() is useful to get a quick glance at the data
# it will provide several metrics (count, mean, std, min, max...)
df.describe()

# Change the indexes for the rows with index()
df.index = ["ROW1", "ROW2"]

df.head()  # First 5 rows of data
df.head(n) # First n rows of data

# hist() can be used to get a histogram of a specific column or Series
df.hist('Column1')

# scatter() can be used to get a scatter diagram of 2 given columns or Series
df.plot.scatter('Column1', 'Column2')

# Locating data in a DataFrame
# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
# Use single or double brackets to obtain Series or DataFrames
df['Column3']       # Column as a Series
df[['Column3']]     # Column as a DataFrame
df[["Column1", "Column4"]] # New Dataframe out of specific columns

df['Column2'][1]    # 2nd element of Column2
df[0:2]             # DataFrame from the first 2 columns of df
# Remember that 0:2 will have 2 columns. It is a closed-open range
# In mathematical terms: [0,2) = [0,1]
sliced_df = df[0:3, 1:10]   # Grabs the first 3 columns, 2nd to 10th rows

# loc is used to locate data with row indexes and column headers
df.loc[0, "Column1"]  # => Row1, with only Column1's value
df.loc[0, "NotAColumn"]  # => KeyError
df.loc[0] # => Row1 entirely

# iloc does the same but using only integers
df.iloc[0, 0]  # => Row1
df.iloc[0, 4000]  # IndexError
df.iloc[:, 0:4] # All rows, only the first 3 columns

# Unique finds each individual value
df["Column2"].unique()  # => 1,2,3

#Filtering by value can also be done
df["Column2"] >= 2  # => 2, 3
df1 = df[df["Column2"] >= 2]
df1 = df[df.column2.isin([1, 4])] # Multiple explicit values for one column
df1 = df[(df["Column2"] == 1) & (df["Column3"] == "some string")] # Multiple-column filtering

# Operating with values
# Operations can be done to columns/Series, so they are applied to each value
df["Column2"] * 5 # => [5, 10, 15]

# Drop specific columns
df_1 = df.copy()
df_1 = df_1.drop(df_1.columns[-9:-5], axis=1)

# apply() is a strong tool which accepts lambda functions
df["Column2"].apply(lambda val: val > 2) # => [3]

####################################################
## 5.2 NumPy
####################################################
# NumPy is a module adding support for large, multi-dimensional arrays
# and matrices, along with a large collection of high-level mathematical
# functions to operate on these arrays.
import numpy as np

array = np.array([0,1,2,3,4]) # creating a 1-dimensional ndarray, the basic NumPy array. It works
# as a usual array would, and can only take one data type

a[3] # => 3
array.size # => 5
array.dim # => 1
array.shape # => (5,) gives the size of the array for each dimension, in a tuple
            # (rows, columns)
array.dtype # => dtype('int64')
type(array) # => numpy.ndarray

# NumPy can perform vector operations much faster than normal Python can
u = np.array([1,0])
v = np.array([0,1])
y = np.array([1,2])

# Addition and subtraction
z = u + v # =>z is now the ndarray [1,1]
z = u - v # => [1,-1]

# Scalar multiplication, addition and subtraction
z = 2 * y # => [2,4]
z = u + 1 #=> [2,1]

# Hadamard product (matrices of same dimensions)
z = v*y  # => [0,2]

# Dot product (a measure of how similar 2 vectors are)
z = np.dot(u, v)  # => 1*0 + 0*1 = 0
z = np.dot(u, y)  # => 1*1 + 0*2 = 1

# Universal functions are functions that work on ndarrays
array.mean()  # => 2
array.max()
b = np.array([0, np.pi/2, np.pi])
np.sin(b)  # [0,1,0]

# linspace can be used to create an evenly-distributed array
# given a starting and finishing point and number of elements
np.linspace(0, 5, num=6)  # => [0,1,2,3,4,5]
np.linspace(-2, 2, num=9)  # => [-2, -1.5, -1, -0.5. 0, 0.5, 1, 1.5, 2]


# Arrays can be 2-Dimensional as well
array = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
array.ndim  # => 2
array.shape # (3,3) where the first number is the number of lists (rows),
            # the second the number of elements in each list (columns)
array.size  # => 9 (3x3)
b = np.array([[1, 0, 1], [0, 1, 1]])
b.shape # => (2,3)
b.size  # => 6

# And as with 1-D arrays, they can be operated upon, just like matrices
# The only particular operation is matrix multiplication
x = np.array([[0, 1, 1], [1, 0, 1]])
y = np.array([[1, 1], [1, 1], [-1, 1]])
# since x's rows must equal y's columns
mult = np.dot(x, y)  # => [[0,0], [0,2]]

####################################################
## 5.3 Keras
####################################################


####################################################
## 6. Classes
####################################################

# We use the "class" statement to create a class
class Human:

    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by Python but that live in user-controlled
    # namespaces. Methods(or objects or attributes) like: __init__, __str__,
    # __repr__ etc. are called special methods (or sometimes called dunder methods)
    # You should not invent such names on your own.
    # __init__() is an initializer, NOT a constructor as in other languages.
    # The object already exists, __init__ only gives values to attributes
    def __init__(self, name):
        self.name = name # Assign the argument to the instance's name attribute

        # Initialize property
        self._age = 0

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # Another instance method
    def sing(self):
        return 'yo... yo... microphone check... one two... one two...'

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method can be called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into an read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age


# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this
# module is the main program.
if __name__ == '__main__':
    # Instantiate a class, creating an object of said class
    i = Human(name="Ian")
    i.say("hi")                     # "Ian: hi"
    Human.say(i, "hi")              # Completely equivalent
    j = Human("Joel")
    j.say("hello")                  # "Joel: hello"

    # Call our class method
    i.say(i.get_species())          # "Ian: H. sapiens"
    # Change the shared attribute
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())          # => "Ian: H. neanderthalensis"
    j.say(j.get_species())          # => "Joel: H. neanderthalensis"

    # Call the static method
    print(Human.grunt())            # => "*grunt*"

    # Cannot call static method with instance of object because i.grunt() will automatically put "self" (the object i) as an argument
    print(i.grunt())                # => TypeError: grunt() takes 0 positional arguments but 1 was given

    # Update the property for this instance
    i.age = 42
    # Get the property
    i.say(i.age)                    # => "Ian: 42"
    j.say(j.age)                    # => "Joel: 0"
    # Delete the property
    del i.age
    # i.age                         # => this would raise an AttributeError

# Objects can be compared by value and by identity
# Value comparison can be done programmatically,
# whereas identity comparison is carried out by the language itself 
r = [1, 2, 3]
s = r
print(r is s) # => True
s = [1, 2, 3]
print(r is s) # => False, they have different identities
print(r == s) # => True, they have the same value
####################################################
## 6.1 Inheritance
####################################################

# Inheritance allows new child classes to be defined that inherit methods and
# variables from their parent class.

# Using the Human class defined above as the base or parent class, we can
# define a child class, Superhero, which inherits the class variables like
# "species", "name", and "age", as well as methods, like "sing" and "grunt"
# from the Human class, but can also have its own unique properties.

# To take advantage of modularization by file you could place the classes above in their own files,
# say, human.py

# To import functions from other files use the following format
# from "filename-without-extension" import "function-or-class"

from human import Human


# Specify the parent class(es) as parameters to the class definition
class Superhero(Human):

    # If the child class should inherit all of the parent's definitions without
    # any modifications, you can just use the "pass" keyword (and nothing else)
    # but in this case it is commented out to allow for a unique child class:
    # pass

    # Child classes can override their parents' attributes
    species = 'Superhuman'

    # Children automatically inherit their parent class's constructor including
    # its arguments, but can also define additional arguments or definitions
    # and override its methods such as the class constructor.
    # This constructor inherits the "name" argument from the "Human" class and
    # adds the "superpower" and "movie" arguments:
    def __init__(self, name, movie=False,
                 superpowers=["super strength", "bulletproofing"]):

        # add additional class attributes:
        self.fictional = True
        self.movie = movie
        # be aware of mutable default values, since defaults are shared
        self.superpowers = superpowers

        # The "super" function lets you access the parent class's methods
        # that are overridden by the child, in this case, the __init__ method.
        # This calls the parent class constructor:
        super().__init__(name)

    # override the sing method
    def sing(self):
        return 'Dun, dun, DUN!'

    # add an additional instance method
    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow=power))


if __name__ == '__main__':
    sup = Superhero(name="Tick")

    # Instance type checks
    if isinstance(sup, Human):
        print('I am human')
    if type(sup) is Superhero:
        print('I am a superhero')

    # Get the Method Resolution search Order used by both getattr() and super()
    # This attribute is dynamic and can be updated
    print(Superhero.__mro__)    # => (<class '__main__.Superhero'>,
                                # => <class 'human.Human'>, <class 'object'>)

    # Calls parent method but uses its own class attribute
    print(sup.get_species())    # => Superhuman

    # Calls overridden method
    print(sup.sing())           # => Dun, dun, DUN!

    # Calls method from Human
    sup.say('Spoon')            # => Tick: Spoon

    # Call method that exists only in Superhero
    sup.boast()                 # => I wield the power of super strength!
                                # => I wield the power of bulletproofing!

    # Inherited class attribute
    sup.age = 31
    print(sup.age)              # => 31

    # Attribute that only exists within Superhero
    print('Am I Oscar eligible? ' + str(sup.movie))

####################################################
## 6.2 Multiple Inheritance
####################################################

# Another class definition
# bat.py
class Bat:

    species = 'Baty'

    def __init__(self, can_fly=True):
        self.fly = can_fly

    # This class also has a say method
    def say(self, msg):
        msg = '... ... ...'
        return msg

    # And its own method as well
    def sonar(self):
        return '))) ... ((('

if __name__ == '__main__':
    b = Bat()
    print(b.say('hello'))
    print(b.fly)


# And yet another class definition that inherits from Superhero and Bat
# superhero.py
from superhero import Superhero
from bat import Bat

# Define Batman as a child that inherits from both Superhero and Bat
class Batman(Superhero, Bat):

    def __init__(self, *args, **kwargs):
        # Typically to inherit attributes you have to call super:
        # super(Batman, self).__init__(*args, **kwargs)      
        # However we are dealing with multiple inheritance here, and super()
        # only works with the next base class in the MRO list.
        # So instead we explicitly call __init__ for all ancestors.
        # The use of *args and **kwargs allows for a clean way to pass arguments,
        # with each parent "peeling a layer of the onion".
        Superhero.__init__(self, 'anonymous', movie=True,
                           superpowers=['Wealthy'], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # override the value for the name attribute
        self.name = 'Sad Affleck'

    def sing(self):
        return 'nan nan nan nan nan batman!'


if __name__ == '__main__':
    sup = Batman()

    # Get the Method Resolution search Order used by both getattr() and super().
    # This attribute is dynamic and can be updated
    print(Batman.__mro__)       # => (<class '__main__.Batman'>,
                                # => <class 'superhero.Superhero'>,
                                # => <class 'human.Human'>,
                                # => <class 'bat.Bat'>, <class 'object'>)

    # Calls parent method but uses its own class attribute
    print(sup.get_species())    # => Superhuman

    # Calls overridden method
    print(sup.sing())           # => nan nan nan nan nan batman!

    # Calls method from Human, because inheritance order matters
    sup.say('I agree')          # => Sad Affleck: I agree

    # Call method that exists only in 2nd ancestor
    print(sup.sonar())          # => ))) ... (((

    # Inherited class attribute
    sup.age = 100
    print(sup.age)              # => 100

    # Inherited attribute from 2nd ancestor whose default value was overridden.
    print('Can I fly? ' + str(sup.fly)) # => Can I fly? False



####################################################
## 7. File Management
####################################################

# Files in Python can be read or written to, as well as updated, supporting
# either binary or encoded text files. By default, files are open to read text
# The best syntax is the following:
with open("filename", "mode", "encoding") as f:
    # Operate with the file, it'll be closed once done
    f.read()

# But you can also use the old way
f  = open("filename", "mode", "encoding")
# Remember to close files once done if you chose this
f.close()
"""
Modes can be:
    r - Read (default)
    w - Write. Overwrites if already exists, creates if not
    a - Append. Creates if non-existant
    x - Exclusive creation. If the file already exists, it fails
    + - Update (read & write)
    
    t - Text mode (default)
    b - Binary mode (using bytes objects)

These 2 blocks can actually be combined, e.g. "r+b", "a", "xb", "+"
"""

with open("filename", "mode", "encoding") as f:    
# Files can be read with read() or written to with write()
    f.read(5) # Reads 5 characters, and moves the reader pointer
    f.readline() # A more elegant way to read entire lines individually
    f.readlines() # Returns a list with every line in the file
    f.write("This is a string") # Writes with the specified encoding
    f.writelines(["This is a\n", "list of strings"]) # Writes without newlines
            # unless added in by hand

# To relocate the pointer to a specific position, use seek()
    f.seek(0) # Returns to first character


####################################################
## 8. Advanced
####################################################

# Generators help you make lazy code. Generators must have at least 1 "yield"
# and can have return statements too. They create single-use generator objects
# which are equal to iterators
def double_numbers(iterable):
    for i in iterable:
        yield i + i

# Generators are memory-efficient because they only load the data needed to
# process the next value in the iterable. This allows them to perform
# operations on otherwise prohibitively large value ranges. This is called
# "lazy" loading
# NOTE: `range` replaces `xrange` in Python 3.
for i in double_numbers(range(1, 900000000)):  # `range` is a generator.
    print(i)
    if i >= 30:
        break

# Just as you can create a list comprehension, you can create generator
# comprehensions as well using parentheses.
values = (-x for x in [1, 2, 3, 4, 5])
for x in values:
    print(x)  # prints -1 -2 -3 -4 -5 to console/terminal

# You can also cast a generator comprehension directly to a list.
values = (-x for x in [1, 2, 3, 4, 5])
gen_to_list = list(values)
print(gen_to_list)  # => [-1, -2, -3, -4, -5]


# The zip() function takes 0 or more iterables, aggregates them in a tuple,
# element by element (first element from all iterables, then second,
# etc), and returns an iterator of said tuples
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three', 'four']
# 'four' will never have a pair, since number_list only goes up to 3

print(list(zip())) # => []
zip_result = zip(number_list, str_list)
print(set(zip_result)) # => {(2, 'two'), (1, 'one'), (3, 'three')} (order is random)
print(list(zip_result)) # => [(1, 'one'), (2, 'two'), (3, 'three')]

# zip can also be used to unzip collections into tuples
numbers, names = zip(list(zip_result))
numbers # => (1, 2, 3)
names # => ('one', 'two', 'three')

# Cartesian product using itertools:
import itertools

somelists = [[1, 2, 3],['a', 'b'],[4, 5]]
list(itertools.product(*somelists))


# Decorators
# In this example `beg` wraps `say`. If say_please is True then it
# will change the returned message.
from functools import wraps

def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    return "Can you buy me a beer?", say_please


print(say())                 # Can you buy me a beer?
print(say(say_please=True))  # Can you buy me a beer? Please! I am poor :(

####################################################
## 9. Testing
####################################################
# Automated tests are a fantastic way to ensure code works even after changes
# are pushed, and to keep things running without spending hours manually
# checking for errors in menial tasks

# Python includes the module unittest not only for Unit Tests, but many others
import unittest

# Define a class which inherits from the type of test you want
class Some_Testing_Class(unittest.TestCase):
    # You can perform set ups and tear downs per test method
    def setUp(self):
        # Create objects, open files...
        pass
    
    # And define the tests inside the class, always prefixing with "test_"
    def test_something(self):
        # Perform the test itself with the included tools, such as assertions
        self.assertEqual(some_function(), 4) # Fails if the function doesn't
                        # return 4. Other types are asertTrue, asertRaises...
        pass
        
    def tearDown(self):
        # Delete objects, close files...
        pass
    
if __name__ == "__main__":
    unittest.main()
    
# And all tests included in the class will be run when the file containing
# this class is run


####################################################
## 10. APIs
####################################################
# APIs allow different programs or code written in other languages
# to communicate with yours through sets of methods, or interfaces.
# REST APIs (REpresentational State Transfer) work over internet
# protocols, usually HTTP with JSON messages, though it may vary.
