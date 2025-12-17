#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:07:40 2023

@author: maria
"""


def read_data(name : str):
    """
    Reads a data file and saves every line as an element of a list
    The line break at the end of a line is sliced away, so the elements do not have a line break at the end

    Parameters
    ----------
    name : str
        Name of the data file.

    Returns
    -------
    data : list[str]
        list where each line of the data file (without the line break) is an element.

    """
    
    data = []
    f = open(name, 'r')
    
    for line in f:
        line = line[:-1]
        data.append(line)
    return data


def format_data(data : list[str]):
    """
    Formats the input data into a useful format.
    input data structure: ['light-to-temperature map:', '29 56 57','humidity-to-location map:', '67 33 62', '33 78 65']
    return list structure: 
        [light-to-temperature list, humidity-to-location list] = [[['29', '56', '57']], [['67', '33', '62'], ['33', '78', '65']]]

    Parameters
    ----------
    data : list[str]
        input data

    Returns
    -------
    list
        a list containing the lists associated with the mappings
        the mapping lists contain lists for every line that corresponds to the data
        Those lists contain the values as elements
        
        structure: list[lists[lines[values]]]

    """
    
    seeds = []
    se_so = []
    so_fe = []
    fe_wa = []
    wa_li = []
    li_te = []
    te_hu = []
    hu_lo = []
    
    seed_line = data[0]
    colon_index = seed_line.find(':')
    
    seed_nums = seed_line[colon_index + 2:]
    seeds = str_to_elements(seed_nums, seeds, ' ')
    
    se_so_index = find_index(data, 'seed-to-soil map:')
    so_fe_index = find_index(data, 'soil-to-fertilizer map:')
    fe_wa_index = find_index(data, 'fertilizer-to-water map:')
    wa_li_index = find_index(data, 'water-to-light map:')
    li_te_index = find_index(data, 'light-to-temperature map:')
    te_hu_index = find_index(data, 'temperature-to-humidity map:')
    hu_lo_index = find_index(data, 'humidity-to-location map:')
    
    for i in range(se_so_index + 1, so_fe_index - 1):
        se_so.append(str_to_elements(data[i], [], ' '))
    
    for i in range(so_fe_index + 1, fe_wa_index - 1):
        so_fe.append(str_to_elements(data[i], [], ' '))
    
    for i in range(fe_wa_index + 1, wa_li_index - 1):
        fe_wa.append(str_to_elements(data[i], [], ' '))
    
    for i in range(wa_li_index + 1, li_te_index - 1):
        wa_li.append(str_to_elements(data[i], [], ' '))
    
    for i in range(li_te_index + 1, te_hu_index - 1):
        li_te.append(str_to_elements(data[i], [], ' '))
    
    for i in range(te_hu_index + 1, hu_lo_index - 1):
        te_hu.append(str_to_elements(data[i], [], ' '))
    
    for i in range(hu_lo_index + 1, len(data)):
        hu_lo.append(str_to_elements(data[i], [], ' '))
    
    
    return [seeds, se_so, so_fe, fe_wa, wa_li, li_te, te_hu, hu_lo]



def str_to_elements(string : str, dest : list, seperator : str):
    """
    Appends the elements in a string to a given list by splitting the string with the given seperator
    input string structure: 'ele1 ele2 ele3 ele4'
    seperator: ' '
    dest list structure: ['ele1', 'ele2', 'ele3', 'ele4']

    Parameters
    ----------
    string : str
        string of elements that are seperated by a common symbol (the seperator)
    dest : list
        the list that the individual elements are appended to
    seperator : str
        the symbol that seperates the elements inside the given string

    Returns
    -------
    dest : list
        list where the elements are the elements of the string

    """
    
    if string == "" or string == " ":
        return dest
    
    one_more_element = True
    
    while one_more_element:
        
        sep_index = string.find(seperator)
        
        if sep_index == -1:
            one_more_element = False
            dest.append(string)
        
        else:
            new_element = string[:sep_index]
            dest.append(new_element)
            string = string[sep_index + 1:]
    
    return dest



def find_index(data : list[str], target : str):
    """
    finds the index of an element in a given list
    input data structure: ['ele1', 'ele2', 'ele3']
    target = 'ele3'
    returns: index = 2

    Parameters
    ----------
    data : list[str]
        list where the elements are strings
    target : str
        the element that is being searched in data

    Returns
    -------
    index : int
        index of the target position in data

    """
    
    index = -1
    
    for i in range(len(data)):
        if data[i] == target:
            index = i
        else:
            continue
    
    return index


def convert_numbers(mapping : list[list], target : str):
    
    target = int(target)
    
    map_num = target
    
    for i in range(len(mapping)):
        
        if target >= int(mapping[i][1]) and target <= (int(mapping[i][1]) + int(mapping[i][2]) - 1):
            map_index = target - int(mapping[i][1])
            map_num = int(mapping[i][0]) + map_index
    
    return str(map_num)



def seed_to_location(data : list[str], mappings, target : str):
    
    conv_to_soil = convert_numbers(mappings[1], target)
    
    conv_to_fertilizer = convert_numbers(mappings[2], conv_to_soil)
    
    conv_to_water = convert_numbers(mappings[3], conv_to_fertilizer)
    
    conv_to_light = convert_numbers(mappings[4], conv_to_water)
    
    conv_to_temperature = convert_numbers(mappings[5], conv_to_light)
    
    conv_to_humidity = convert_numbers(mappings[6], conv_to_temperature)
    
    conv_to_location = convert_numbers(mappings[7], conv_to_humidity)
    
    return conv_to_location


def get_seeds(data : list[str]):
    
    seeds = []
    
    seed_line = data[0]
    colon_index = seed_line.find(':')
    
    seed_nums = seed_line[colon_index + 2:]
    seeds = str_to_elements(seed_nums, seeds, ' ')
    
    return seeds


def find_minimum(llist : list[int]):
    
    minimum = llist[0]
    
    for i in llist:
        if i < minimum:
            minimum = i
    
    return minimum



################# read data ####################

data = read_data("Seed_data.txt")

# for i in data:
#     print(i)

mappings = format_data(data)

################# Task 1 #######################
"""
seeds = get_seeds(data)
locations = []

for i in seeds:
    location = seed_to_location(data, mappings, i)
    locations.append(int(location))

print(locations)

min_location = find_minimum(locations)

print(min_location)
"""


################# Task 2 #######################

seeds = get_seeds(data)
locations = []
# one_more_range = True
# i = 0



# while one_more_range:
#     if i >= len(seeds):
#         one_more_element = False
#         break
#     else:
#         for j in range(int(seeds[i]), int(seeds[i]) + int(seeds[i+1])):
#             location = seed_to_location(data, mappings, str(j))
#             locations.append(location)
#     i += 2

# for i in range(int(seeds[0]), int(seeds[0])+int(seeds[1])):
#     print(i)
#     location = seed_to_location(data, mappings, str(i))
#     locations.append(location)

# min_location = find_minimum(locations)

# print(min_location)

initial_seeds = []
for i in range(len(seeds)):
    if i % 2 == 0:
        initial_seeds.append(seeds[i])

print(initial_seeds)

for i in initial_seeds:
    location = seed_to_location(data, mappings, i)
    locations.append(int(location))

print(locations)

min_location = find_minimum(locations)

print(min_location)



"""
Useful information to check if the functions work

mappings = format_data(data)
seeds = mappings[0] 
se_so = mappings[1] 
so_fe = mappings[2]
fe_wa = mappings[3]
wa_li = mappings[4]
li_te = mappings[5]
te_hu = mappings[6]
hu_lo = mappings[7]


#print(seeds)
for i in range(8):
    print(mappings[i])



converted_seed_to_soil = convert_numbers(se_so, '79')
print(converted_seed_to_soil)

converted_seed_to_soil2 = convert_numbers(se_so, '14')
print(converted_seed_to_soil2)

converted_seed_to_soil3 = convert_numbers(se_so, '55')
print(converted_seed_to_soil3)

converted_seed_to_soil4 = convert_numbers(se_so, '13')
print(converted_seed_to_soil4)

"""

#location = seed_to_location(data, '13')
#print(location)



