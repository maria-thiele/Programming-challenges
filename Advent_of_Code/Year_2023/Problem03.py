#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:41:04 2023

@author: maria
"""

"""
Day 3 :
    The tasks were based on a schematic.
    The data set consisted of several lines that contained numbers, dots and other symbols.
    The first problem asked for the sum of all the numbers that were adjacent to a symbol 
    (also diagonally, dots are not considered symbols)
    The second problem was about the sum of the gear ratios.
    A gear was the product of the two adjacent numbers of a star *
    A gear can only be calculated if the star is adjacent to exactly two numbers.

Remark :
    The documentation was last changed on the 14.12.2023
    It is supposed to help understand the code but might lack some coherence and detail.

This code produced the correct answers.
"""

def get_symbols(data : list[str]):
    """
    Gathers all symbols that are not numbers or dots in a list

    Parameters
    ----------
    data : list[str]
        data input, a file containing rows of numbers, dots and symbols

    Returns
    -------
    symbols : list[str]
        list of all the symbols in the data
    """
    
    symbols = []
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for element in data:
        for i in element:
            if i != "." and i not in numbers:
                if i not in symbols:
                    symbols.append(i)
                continue
    
    return symbols


def get_part_numbers(data : list[str], symbols : list[str]):
    """
    Gets the numbers that are adjacent to a symbol

    Parameters
    ----------
    data : list[str]
        data input, a file containing rows of numbers, dots and symbols.
    symbols : list[str]
        all different symbols in the data.

    Returns
    -------
    part_numbers : list[str]
        list of all numbers adjacent to a symbol.

    """
    
    part_numbers = []
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    # check for every line in the data file
    for element in data:
        
        i = 0
        while i <= len(element) - 1:
            counter = 0
            
            # get complete numbers
            if element[i] in numbers:
                
                num = element[i]
                j = i + 1
                one_more_number = True
                
                # iterate over next elements as long as a character is no longer a number
                while one_more_number and j<=len(element) - 1:
                    
                    if element[j] in numbers:
                        counter += 1
                        num += element[j]
                        
                    else:
                        one_more_number = False
                    j += 1
                
                # check if the number is adjacent to a symbol
                is_part = check_for_symbol(data, symbols, element, i, i + counter)
                
                if is_part == True:
                    part_numbers.append(num)
                
            # jump to the index after a number has ended (or just increase by one if counter = 0)
            i += counter + 1

    return part_numbers


def check_for_symbol(data : list[str], symbols : list[str], line : str, start : int, stop : int):
    """
    The function checks if a symbol is present in a specific line in a specific index range

    Parameters
    ----------
    data : list[str]
        data input, a file containing rows of numbers, dots and symbols.
    symbols : list[str]
        all different symbols in the data.
    line : str
        The line of the number.
    start : int
        index in the line where the number starts.
    stop : int
        index in the line where the number stops.

    Returns
    -------
    is_part : boolean
        True, when there is a symbol adjacent to the number and False, if there is not.

    """
    
    line_index = 0
    is_part = False
    
    # search for the index of the line in the data
    for index in range(len(data)):
        if data[index] == line:
            line_index = index
    
    # define new starting and ending indices (diagonally counts as well)
    if start != 0:
        new_start = start - 1
    else:
        new_start = start
    
    if stop != len(data) - 1:
        new_stop = stop + 1
    else:
        new_stop = stop
    
    
    # check line above if possible
    if line_index != 0:
        element = data[line_index - 1]
        for i in range(new_start, new_stop + 1):
            if element[i] in symbols:
                is_part = True
                return is_part
    
    # check line below if possible
    if line_index != len(data) - 1:
        element = data[line_index + 1]
        for i in range(new_start, new_stop + 1):
            if element[i] in symbols:
                is_part = True
                return is_part
    
    # check before and after if possible
    if line[new_start] in symbols or line[new_stop] in symbols:
        is_part = True
        return is_part
    
    return is_part


def get_numbers(data : list[str]):
    """
    Creates and returns a dictionary that contains all the numbers in the data.
    The values of the dictionary are the numbers, the keys are their respective identification numbers
    An identification number is made up as follows: line, start, stop
    where line is the index of the line the number is in,
    start is the index in the line where the number starts and stop is the index where it ends

    Parameters
    ----------
    data : list[str]
        data input, a file containing rows of numbers, dots and symbols

    Returns
    -------
    numbers_dict : dict
        dictionary containing all the numbers and identification numbers
    """
    numbers_dict = {}
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    index_counter = -1
    
    for element in data:
        index_counter += 1
        
        i = 0
        
        while i <= len(element) - 1:
            
            counter = 0
            
            if element[i] in numbers:
                
                num = element[i]
                
                j = i + 1
                one_more_number = True
                
                while one_more_number and j<=len(element) - 1:
                    
                    if element[j] in numbers:
                        counter += 1
                        num += element[j]
                        
                    else:
                        one_more_number = False
                    j += 1
                
                num_id = get_identification(index_counter, i, i + counter)
                
                numbers_dict[num_id] = int(num)
                
            i += counter + 1
    
    return numbers_dict


def get_identification(line : int, start : int, stop : int):
    """
    Computes the identification number of a number in the data
    The format of the string is: line, start, stop
    line is the index of the line in the data 
    and start and stop are the beginning and ending indices of the number in the line

    Parameters
    ----------
    line : int
        index of the line
    start : int
        starting index of the number in the line
    stop : int
        ending index of the number in the line

    Returns
    -------
    id_num : str
        the string of the identification number

    """
    
    line_str = str(line)
    start_str = str(start)
    stop_str = str(stop)
    
    id_num = line_str + "," + start_str + "," + stop_str
    
    return id_num


def get_star_position(data : list[str]):
    """
    Returns a dictionary that contains the positions of stars as keys and a counter as a value
    the counter is set to 0 by default
    The position follows the format: line, index
    line describes the line of the data and index is the position in the line

    Parameters
    ----------
    data : list[str]
        data input, a file containing rows of numbers, dots and symbols

    Returns
    -------
    stars : dict
        a dictionary with a string describing the position of a star as keys and 0s as values

    """
    
    stars = {}
    
    line_counter = -1
    
    for element in data:
        line_counter += 1
        
        for index in range(len(element)):
            
            if element[index] == "*":
                key = str(line_counter) + "," + str(index)
                stars[key] = 0
    
    return stars


def check_number_next_star(numbers : dict, star_pos : str):
    """
    Stores all the numbers adjacent to a star in a list

    Parameters
    ----------
    numbers : dict
        dictionary of the identification position of a number and the value of the number
    star_pos : str
        string describing the position of a star in the data

    Returns
    -------
    list_numbers : list
        list of all adjacent numbers

    """
    
    list_numbers = []
    
    comma_index = star_pos.find(",")
    line = int(star_pos[:comma_index])
    position = int(star_pos[comma_index + 1:])
    
    
    if line != 0:
        list_numbers = check_line(numbers, line - 1, position, list_numbers)
    
    
    list_numbers = check_line(numbers, line, position, list_numbers)
    
    list_numbers = check_line(numbers, line + 1, position, list_numbers)
    
    return list_numbers



def check_line(numbers : dict, line : int, star_pos : int, list_nums : list):
    """
    Checks a specific line for adjacent numbers to a star

    Parameters
    ----------
    numbers : dict
        dictionary of the identification position of a number and the value of the number
    line : int
        index of line to be checked
    star_pos : int
        index of the position of the star
    list_nums : list
        list of all adjacent numbers so far

    Returns
    -------
    list_nums : list
        appended list of all adjacent numbers so far plus adjacent numbers of the current line

    """
    
    nums_in_line = []
    
    for pos in numbers.keys():
        
        first_comma = pos.find(",")
        num_line = int(pos[:first_comma])
        
        if num_line == line:
            nums_in_line.append(pos)
    
    for i in nums_in_line:
        
        first_comma = i.find(",")
        last_comma = i.rfind(",")
        
        start = int(i[first_comma + 1:last_comma])
        stop = int(i[last_comma + 1:])
        
        if start <= star_pos + 1 and stop >= star_pos - 1:
            list_nums.append(i)
    
    return list_nums




############## read data ##############
data = []

f = open("Schematic_data.txt", 'r')

for line in f:
    line = line[0:-1]
    data.append(line)

f.close()

for i in data:
    print(i)

############## get all symbols in a list ##############
symbols = get_symbols(data)
#print(symbols)


"""
Problem 1
"""


############## function call to get the part numbers ##############
parts = get_part_numbers(data, symbols)
print(parts)


############## get the sum of the part numbers ##############
s = 0
for i in parts:
    s += int(i)

print(s)


"""
Problem 2
"""

nums = get_numbers(data)

stars = get_star_position(data)

gear_ratios = []

for star in stars.keys():
    number_num = check_number_next_star(nums, star)
    
    if len(number_num) == 2:
        first_key = number_num[0]
        second_key = number_num[1]
        
        first_num = nums[first_key]
        second_num = nums[second_key]
        
        ratio = first_num * second_num
        
        gear_ratios.append(ratio)


s = 0

for i in gear_ratios:
    s += i

print(s)


