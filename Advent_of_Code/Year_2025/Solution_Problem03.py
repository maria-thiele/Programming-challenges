"""
Advent of Code challenge 
Year 2025

Day 3 :
    In this problem the input data consists of several lines that each contain a sequence of digits.
    The goal is to find the largest 2-digit number that can be extracted from each sequence. The order of the digits needs to be preserved,
    but it is possible to select digits that are not consecutive in the sequence.
    For example, the largest 2-digit number of the sequence '79364' would be '96'.
    
    The soltion is the sum of all of the highest 2-digits numbers from each sequence.
    
    For the second part of the problem, the task is the same, however now the joltages are a 12-digit number.
    Again, the sum of all the highest (here 12-digit) joltages needs to be computed.

Remark :
    This code produced the correct answers.
"""

def max_joltage(data: list[str]) -> int:
    """
    Loops through each sequence of digits and keeps track of the highest digit as well as the last occurences of each digit.
    Based on this the maximum joltage is computed (for the definition of joltage see description at the start).

    Args:
        data (list[str]): list with sequences

    Returns:
        total_joltage (int): sum of the highest joltages of all sequences in data
    """
    
    total_joltage = 0
    
    # loop through each sequence
    for bank in data:
        
        individual_joltages = {} # dictionary that stores the last index of each number
        max_joltage = "0" # keeps track of the first occurence of the highest joltage
        index_max_joltage = -1 # index of the highest joltage
        
        # find the highest digit and keep track of each numbers last occurence
        for index in range(len(bank)):
            joltage = bank[index] # current digit
            
            # update dictionary with the last index for a digit
            individual_joltages[joltage] = index
            
            # update max_joltage if current joltage is larger
            if int(joltage) > int(max_joltage):
                max_joltage = joltage
                index_max_joltage = index
        
        result = ""
        # case: largest digit is at the end of the sequence
        # -> search for the second highest number
        if index_max_joltage == len(bank)-1:
            second_highest = int(max_joltage) - 1
            while second_highest > 0:
                if str(second_highest) in individual_joltages:
                    result = str(second_highest) + max_joltage
                    break
                second_highest - 1
        
        # case: largest digit is not at the end of the sequence
        # -> find the largest digit that comes after the highest digit
        else:
            second_highest = int(max_joltage)
            while second_highest > 0:
                #print("Second highest in loop:", second_highest)
                if str(second_highest) in individual_joltages and individual_joltages[str(second_highest)] > index_max_joltage:
                    result = max_joltage + str(second_highest)
                    break
                second_highest -= 1
        
        #print("Bank:", bank)
        #print("Result:", result)
        total_joltage += int(result)
            
    return total_joltage


def max_joltage_12digit(data: list[str]) -> int:
    """
    Computes the highest 12-digit joltage for a given sequence.
    Idea:   The first digit can be selected out of all digits except the last 11.
            Choose the first occurence of the highest number and discard everything before that occurence.
            Now look at the sequence that starts right after the occurence of the highest number and from this, choose the highest 11-digit joltage.
            This can be done through the same approach as for the 12-digit joltage.
            Repeat until the entire 12-digit joltage is found.

    Args:
        data (list[str]): list with sequences

    Returns:
        total_joltage (int): sum of the highest joltages of all sequences in data
    """
    
    total_joltage = 0
    
    for bank in data:
        #print("Bank:", bank)
        
        sequence = bank
        highest_joltage = ""
        n = 12
        
        while n > 0:
            sequence = n_digit_joltage(sequence, n)
            #print("Sequence:", sequence)
            #print("n:", n)
            highest_joltage += sequence[0]
            
            n -= 1
            sequence = sequence[1:]
        
        #print("Highest joltage:", highest_joltage)
        total_joltage += int(highest_joltage)
    
    return total_joltage


def n_digit_joltage(sequence: str, n: int) -> str:
    """
    Searches for the first digit of the highest n-digit joltage of a sequence.
    The first digit of the highest possible joltage will be in the subsequence of sequence[0:-(n-1)]

    Args:
        sequence (str): sequence of digits
        n (int): size of the joltage

    Returns:
        str: subsequence of sequence starting with the digit for the highest n-digit joltage 
    """
    
    # if the sequence has as many digits as the joltage needs, the highest joltage is the sequence
    if len(sequence) == n:
        return sequence
    
    # determine the highest digit
    highest = "0"
    index_highest = 0
    leftover = len(sequence) - n
    subsequence = sequence[:leftover + 1] # everything until the last n-1 places
    #print("in n-digit sequence:", sequence)
    #print("in n-digit subsequence:", subsequence)
    
    for index in range(len(subsequence)):
        if int(subsequence[index]) > int(highest):
            highest = subsequence[index]
            index_highest = index
    
    # remove everything before the highest found digit
    return sequence[index_highest:]

########### load data ##############

# try with a small dataset
#f = open("Joltage_Data_Small.txt", 'r')

# run for the big dataset
f = open("Joltage_Data.txt", 'r')

data = []

# append every line (without the line break) to a list
for line in f:
    data.append(line.strip())

#print(data)


########### main logic ##############

# part 1
joltage_part1 = max_joltage(data)
print("Total joltage Part 1:", joltage_part1)

# part 2
joltage_part2 = max_joltage_12digit(data)
print("Total joltage Part 2:", joltage_part2)
