"""
Advent of Code challenge 
Year 2025

Day 1 :
    In order to get access to the christmas base a password is needed.
    This password can be obtained by following the instructions in the data document.
    Each line either starts with an 'L' or an 'R' and is followed by a number, so e.g. 'R24' or 'L50'.
    For each instruction that starts with an 'R', the number after the 'R' is added to the current number.
    If the instruction starts with an 'L', the number after the 'L' is subtracted from the current number.
    The valid numbers are the digits on a safe that are arranged in a circle from 0 to 99. 
    So the instruction 'R10' would result in '30' if the current number is '20' and 'L5' would result in '15' for the current number '20'.
    Since numbers are arranged in a circle, the instruction 'L10' given the current number '5' results in '95'.
    Likewise, for a current number of '90', the instruction 'R10' results in '0'.
    
    The goal is to execute the instructions in the data file with a starting number of '50' and count the amount of times an instruction results in the number '0'.
    
    For the second part, the task is slightly changed and now the number of times in which the dial points to '0'
    needs to be counted. Again, the starting number is '50'.

Remark :
    This code produced the correct answers.
"""

def get_password(data: list[str], target: int, start: int) -> int:
    """
    Retrieves the password for the first part by counting the number of times that an instruction stops
    at the target value
    
    Args:
        data (list[str]): input data where each element corresponds to an instruction like 'R10' or 'L5'
        target (int): the number that is counted
        start (int): starting number for the first instruction

    Returns:
        counter (int): amount of times the target was reached
    """
    
    counter = 0
    current = start
    
    for instruction in data:
        direction = instruction[0]  # either an 'R' or an 'L'
        number = int(instruction[1:])
        
        # remove full circles
        while number >= 100:
            number -= 100
        
        # rotate to the right -> numbers are added
        if direction == 'R':
            current += number
            
        # rotate to the left -> numbers are subtracted
        else:
           current -= number 
        
        # check if number is out of bounds and readjust
        if current > 99:
            current -= 100
        elif current < 0:
            current += 100
        
        # count the amount of times the target number is reached after rotations
        if current == target:
            counter += 1    
    
    return counter


def get_updated_password(data: list[str], target: int, start: int) -> int:
    """
    Retrieves the password for the second part by counting the number of times that an instruction points
    at the target value (also counting whenever the target value is reached during an instruction)
    
    Args:
        data (list[str]): input data where each element corresponds to an instruction like 'R10' or 'L5'
        target (int): the number that is counted
        start (int): starting number for the first instruction

    Returns:
        counter (int): amount of times the target was pointed to
    """
    counter = 0
    current = start
    
    for instruction in data:
        direction = instruction[0]  # either an 'R' or an 'L'
        number = int(instruction[1:])
        
        # execute full circles
        while number >= 100:
            number -= 100
            counter += 1
        
        # rotate to the right -> numbers are added
        if direction == 'R':
            temp = current + number
            # check if number is out of bounds and update counter if necessary
            if temp > 99:
                temp -= 100
                if target < temp or target > current:
                    counter += 1
            else:
                if target > current and target < temp:
                    counter += 1
            
        # rotate to the left -> numbers are subtracted
        else:
            temp = current - number
            # check if number is out of bounds and update counter if necessary
            if temp < 0:
                temp += 100
                if target < current or target > temp:
                    counter += 1
            else:
                if target < current and target > temp:
                    counter += 1

        current = temp
        
        # count the amount of times the target number is reached after rotations
        if current == target:
            counter += 1    
    
    return counter


########### load data ##############

# try with a small dataset
#f = open("Password_Data_Small.txt", 'r')

# run for the big dataset
f = open("Password_Data.txt", 'r')
data = []

# append every line (without the line break) to a list
for line in f:
    data.append(line.strip())

#print(data)


########### main logic ##############

# part 1
password1 = get_password(data, 0, 50)
print("Password Part 1:", password1)

# part 2
password2 = get_updated_password(data, 0, 50)
print("Password Part 2:", password2)