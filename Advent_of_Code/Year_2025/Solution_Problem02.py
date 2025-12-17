"""
Advent of Code challenge 
Year 2025

Day 2 :
    This problem is about filtering out invalid IDs.
    An invalid ID is an ID which is made entirely out of a sequence of digits that repeats twice 
    (e.g. 55, 6464, 123123).
    
    Given some ID ranges, the task is to find all invalid IDs within this range and add them up
    (e.g. range 95-115 has 1 invalid ID: 99).
    
    In the second part the definition for an invalid ID is broadened.
    Now every ID that consists only of a sequence of digits that repeats at least two times is unvalid.
    So now the ID '123123123' would also be invalid as it consists of only three times '123'.
    Again, the sum of all invalid IDs needs to be computed.

Remark :
    This code produced the correct answers.
"""

def count_invalid_IDs(data: list[str]) -> int:
    """
    Counts the amount of invalid IDs within a given range and adds them together.
    An invalid ID is an ID that consists only of a sequence of digits that repeats twice.
    
    Args:
        data (list[str]): list where each element is a range of form: start-end

    Returns:
        sum_invalid_IDs (int): sum of all invalid IDs in all of the ranges
    """
    
    sum_invalid_IDs = 0
    
    for range in data:
        #print("Range:", range)
        # split the range into start and end
        interval = range.split('-')
        start = interval[0]
        end = interval[1]
        
        # ranges with only uneven numbers cannot have any unvalid IDs, so they can be skipped
        if (len(start) == len(end) and len(start) % 2 == 1):
            print("Skipped:", start, end)
            continue
        
        current_ID = start
        end_int = int(end)
        
        # loop through all IDs in the range
        while int(current_ID) <= end_int:
            
            # only check if the ID is invalid if the ID has an even length
            if len(current_ID) % 2 == 0:
                half = len(current_ID) // 2
                left = current_ID[:half]
                right = current_ID[half:]
                
                # check if ID is invalid and if so, add to the rest
                if left == right:
                    sum_invalid_IDs += int(current_ID)
            
            # increase the current ID
            current_ID = str(int(current_ID) + 1)
             
    return sum_invalid_IDs


def updated_invalid_IDs(data: list[str]) -> int:
    """
    Counts the amount of invalid IDs within a given range and adds them together.
    An invalid ID is an ID that consists only of a sequence of digits that repeats at least twice.
    
    Args:
        data (list[str]): list where each element is a range of form: start-end

    Returns:
        sum_invalid_IDs (int): sum of all invalid IDs in all of the ranges
    """
    
    sum_invalid_IDs = 0
    
    for range in data:
        #print("Range:", range)
        # split the range into start and end
        interval = range.split('-')
        start = interval[0]
        end = int(interval[1])
        
        current_ID = start
        
        # loop through all IDs in the range
        while int(current_ID) <= end:
            #print("Current ID:", current_ID)
            
            # divide ID in half to get the maximum possible substring that could be repeated
            index = len(current_ID) // 2
            
            # check if ID is made out of a substring
            # start with the largest possible substring and continue with smaller substrings
            while index > 0:
                #print("Index:", index)
                substring = current_ID[0:index]
                #print("Substring:", substring)
                #print("Rest:", current_ID[index:])
                is_invalid = check_substring(substring, current_ID[index:])
                
                # check if ID is invalid and if so, add to the rest
                if is_invalid:
                    sum_invalid_IDs += int(current_ID)
                    break
                
                index -= 1
            
            # increase the current ID
            current_ID = str(int(current_ID) + 1)
             
    return sum_invalid_IDs

def check_substring(substring: str, string: str) -> bool:
    """
    Checks if a given string only consists of the sequence of characters of the substring

    Args:
        substring (str): given substring
        string (str): string eventually made up of the substring

    Returns:
        bool: True, when the string is completely made out of the substring
              False, when the sring is not just made out of the substring
    """
    is_substring = False
    
    # loop through the string and check if it consists only of the substring
    while len(substring) <= len(string): # break loop when there are less characters in string then in substring
        #print("In while loop in check_substring")
        # check if the next n characters are the same as the n character long substring
        next_substring = string[0:len(substring)]
        #print("Next Sub:", next_substring)
        
        # break the loop when the two substrings are unequal
        if next_substring != substring:
            return is_substring
        else:
            # if they are equal and they are the last characters in string, the string was made out of the substring
            # if they dont have the same length, slice the string to only have the remainder of characters not yet checked
            if len(string) == len(substring):
                is_substring = True
                return is_substring
            else:
                string = string[len(substring):]
    
    return is_substring

########### load data ##############

# try with a small dataset
#f = open("ID_Data_Examples.txt", 'r')

# run for the big dataset
f = open("ID_Data.txt", 'r')

data = []

# append every line (without the line break) to a list
for line in f:
    data = line.split(',')

print(data)


########### main logic ##############

# part 1
sum_invalid_part1 = count_invalid_IDs(data)
print("Invalid Ids Part 1:", sum_invalid_part1)

# part 2
sum_invalid_part2 = updated_invalid_IDs(data)
print("Invalid Ids Part 2:", sum_invalid_part2)