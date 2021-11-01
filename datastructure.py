#Data Structures and Algorithms

"""
Unpacking a Sequence into Separate Variables
"""
#Any sequence can be unpacked into variables using a simple assignment operation'
raw_data = ['TSLA', 1000, (2021, 11,1)]
instrument_name, price, (year, month, day) = raw_data
print(price)
print(month)
