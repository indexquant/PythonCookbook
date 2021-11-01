#Data Structures and Algorithms

"""
============================================
1. Unpacking a Sequence into Separate Variables
============================================
"""
#Any sequence can be unpacked into variables using a simple assignment operation'
raw_data = ['TSLA', 1000, (2021, 11,1)]
instrument_name, price, (year, month, day) = raw_data
print(price)
print(month)

#if you want to discard certain values
_, price, (year, month, day) = raw_data