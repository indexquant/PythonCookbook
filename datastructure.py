"""
Python Self Cookbook

last update : 1 Nov 2021
The curriculum and script ideas are mainly sourced from "Python Cookbook by David Beazley & Brian K.Jones (O'Reilly)
================================================================
Table of Contents (# of sub-topics):

1. Data Structures and Algorithms (20)
2. Strings and Text (20)
3. Numbers, Dates, and Times (16)
4. Iterators and Generators (16)
5. Files and I/O (21)
6. Data Encoding and Processing (13)
7. Functions (12)
8. Classes and Objects (25)

Some advanced topics may be included:
Metaprogramming, Modules and Packages, Network and Web Programming, Concurrency, Utility Scripting and System Admin, Testing/Debugging/Exceptions, C Extension
================================================================


================================================================
1. Data Structures and Algorithms
================================================================
"""


######### Unpacking a Sequence into Separate Variables #########
#================================================================
#Any sequence can be unpacked into variables using a simple assignment operation'
raw_data = ['TSLA', 1000, (2021, 11,1)]
instrument_name, price, (year, month, day) = raw_data
print(price)
print(month)

#Unpacking works with any object not just tuples or lists.
string = 'Python'
a, b, c, d, e, f = string
print(b)

#if you want to discard certain values
_, price, (year, month, day) = raw_data

