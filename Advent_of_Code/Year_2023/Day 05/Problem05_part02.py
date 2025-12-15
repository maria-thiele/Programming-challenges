#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:03:51 2023

@author: maria
"""

import Problem05_part01 as p
from matplotlib import pyplot as plt

def sort_list(llist: list[int]):
    """
    Sorts the elements of a list in ascending order using recursion.

    Parameters
    ----------
    llist : list[int]
        list with unsorted integer values

    Returns
    -------
    new_list : list[int]
        list with the elements of llist sorted in ascending order

    """
    
    # Base case
    if len(llist) == 0:
        return []
    
    elif len(llist) == 1:
        return llist
    
    # Recursive case
    else:
        new_value = llist[0]
        sorted_list = sort_list(llist[1:])
        
        i = 0
        is_last = False
        
        while new_value > sorted_list[i]:
            
            # ceck if the element is larger than the last element of sorted_arr
            if (i + 1) < len(sorted_list):
                i += 1
            else:
                is_last = True
                break
            
        # the element has to appended at the end of sorted_arr
        if is_last == True:
            new_list = sorted_list + [new_value]
        
        # the element is appended in the middle of sorted_arr
        else:
            new_list = sorted_list[0:i] + [new_value] + sorted_list[i:]
    return new_list



data = p.read_data("Seed_data.txt")

# for i in data:
#     print(i)

mappings = p.format_data(data)

seeds = mappings[0]

seed_range = []

for i in range(len(seeds)):
    if i % 2 == 0:
        seed_range.append(int(seeds[i]))
        seed_range.append(int(seeds[i]) + int(seeds[i+1]) - 1)

sorted_seeds = sort_list(seed_range)

x = []
y = []

# for i in range(264807001, 4250787494, 100000000):
#     x.append(i)
#     location = p.seed_to_location(data, mappings, str(i))
#     y.append(location)

for i in sorted_seeds:
    x.append(i)
    location = p.seed_to_location(data, mappings, str(i))
    y.append(location)
    

x2 = []
y2 = []

for i in sorted_seeds[:5]:
    x2.append(i)
    location = p.seed_to_location(data, mappings, str(i))
    y2.append(location)
    

x3 = []
y3 = []

for i in range(sorted_seeds[0], sorted_seeds[1], 10000000):
    x3.append(i)
    location = p.seed_to_location(data, mappings, str(i))
    y3.append(location)


print("................................................")

#print(seeds)

#print(seed_range)

# for i in sorted_seeds:
#     print(i)

plt.plot(x, y, 'b-')
plt.plot(x, y, 'ro')
plt.plot(x[0], y[0], 'go')
#plt.plot(x2, y2, 'r-')
plt.show()



plt.plot(x3, y3, 'b-')
plt.plot(x3[0], y3[0], 'ro')
plt.show()

lowest = p.seed_to_location(data, mappings, str(x[0]))
print(lowest)










#%%


# order = []

# for element in mappings[7]:
#     order.append(int(element[1]))

# sorted_order = sort_list(order)

# hu_lo = []

# for i in sorted_order:
    
#     for j in mappings[7]:
#         if j[1] == str(i):
#             hu_lo.append(j)
    

# x = []
# y = []

# for i in hu_lo:
#     x1 = int(i[1])
#     y1 = int(i[0])
    
#     x2 = int(i[1]) + int(i[2]) - 1
#     y2 = int(i[0]) + int(i[2]) - 1
    
#     x.append(x1)
#     x.append(x2)
    
#     y.append(y1)
#     y.append(y2)


# plt.plot(x, y)
# plt.plot(x[:len(x)//2], y[:len(y)//2], 'r-')
# #plt.show()

# plt.plot(x[:len(x)//2], y[:len(y)//2], 'r-')
# plt.plot(x[24:26], y[24:26], 'b-')
# plt.show()

# # plt.plot(x[24:26], y[24:26], 'b-')
# # plt.show()

# print(len(x)//2)

# print(x[24:26])
# print(y[24:26])


