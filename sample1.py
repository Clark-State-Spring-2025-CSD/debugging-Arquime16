#This file will be used in the lecture video/class demonstration.

import math

x = 123456789
print(f"Test value is {x}")
test1 = x % 1000
print(f"Channel 1 is : {test1}")
test2 = math.floor(x % 1000000 / 1000)
print(f"Channel 2 is : {test2}")
test3 = math.floor(x % 1000000000 / 1000000)
print(f"Channel 3 is : {test3}")

print("***Calculations***")

channel = 1
testCalc = math.floor(x % (1000**channel) / (1000**(channel - 1)))
print(f"Channel 1 is : {testCalc}")

channel = 2
testCalc = math.floor(x % (1000**channel) / (1000**(channel - 1)))
print(f"Channel 2 is : {testCalc}")

channel = 3
testCalc = math.floor(x % (1000**channel) / (1000**(channel - 1)))
print(f"Channel 3 is : {testCalc}")

