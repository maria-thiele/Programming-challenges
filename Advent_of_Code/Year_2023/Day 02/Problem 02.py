#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:02:45 2023

@author: maria
"""
"""
Day 2 :
    The tasks were based on a game.
    In a bag there are cubes of three different colors.
    Every game, a number of sets of drawings is down. Every set contains the numbers of red, green and blue cubes that were drawn.
    The first task requires to compute the sum of all games that could have been played with a fixed number of cubes for red,...
    In the second task, the sum of the powers of the games had to be computed.
    The power of a game is the product of the number of green, red and blue cubes that had to be in a game to make the game possible.

Remark :
    The documentation was last changed on the 6.12.2023
    It is supposed to help understand the code but might lack some coherence and detail.

This code produced the correct answers.
"""


def str_to_list(s : str, symbol : str):
    """
    Turns information in the string that is separated by a specific symbol into elements of a list

    Parameters
    ----------
    s : str
        string containing information about the color and number of balls.
        The information is seperated by a symbol (comma, semikolon,...) e.g. 2 green, 3 blue

    Returns
    -------
    set_list : list
        list of the information where every element is the color and number of one ball.
        e.g. the example above would give ['2 green', '3 blue']
    """
    
    one_more_element = True
    set_list = []
    
    while one_more_element:
        index_symbol = s.find(symbol)
        
        if index_symbol != -1:
            set_list.append(s[0:index_symbol])
            s = s[index_symbol + 2:]
        
        else:
            set_list.append(s)
            one_more_element = False
    
    return set_list


def possible_games(games : dict):
    """
    Determines how many games are possible based on how many cubes were drawn from the bag

    Parameters
    ----------
    games : dict
        a dictionary were the keys are the game numbers and the values are lists conatining the sets of various drawings of balls.

    Returns
    -------
    sum_possible : int
        the sum of all the possible games.
    """
    
    sum_possible = 0
    
    
    # check the condition of the possible outcomes
    
    for key, value in games.items():
        
        counter_possible = 0        # counts possible sets
        
        for sets in value:
            
            possible = True
            
            for element in sets:
                
                # check the condition for every element in a set
                color_num = 0
                if element.find("green") != -1:
                    index = element.find("green")
                    num = int(element[0: index - 1])
                    color_num = 13
                    
                elif element.find("red") != -1:
                    index = element.find("red")
                    num = int(element[0: index - 1])
                    color_num = 12
                
                elif element.find("blue") != -1:
                    index = element.find("blue")
                    num = int(element[0: index - 1])
                    color_num = 14
                
                # if an element does not fit the conditions, the set is not possible
                if num > color_num:
                    possible = False
                    break
            
            # counts the possible sets
            if possible == True:
                counter_possible += 1
        
        if counter_possible == len(value):      # if the counter has the same length as the list, all sets are possible
            sum_possible += key
            
    return sum_possible


def fewest_number(games : dict):
    """
    Based on the number of balls drwan in a game, the power of the game is calculated by multiplying
    the number of red, green and blue balls.
    The powers of all the games are stored in a list.

    Parameters
    ----------
    games : dict
        dictionary where the keys are the game numbers and the values represent the sets of drawings of a game.

    Returns
    -------
    powers : list
        list of all the powers of the games.

    """
    
    powers = []
    
    for value in games.values():
        
        red = 0
        blue = 0
        green = 0
        
        for sets in value:
            
            for element in sets:
                
                if element.find("green") != -1:
                    index = element.find("green")
                    num = int(element[0: index - 1])
                    
                    if num > green:
                        green = num
                    
                elif element.find("red") != -1:
                    index = element.find("red")
                    num = int(element[0: index - 1])
                    
                    if num > red:
                        red = num
                
                elif element.find("blue") != -1:
                    index = element.find("blue")
                    num = int(element[0: index - 1])
                    
                    if num > blue:
                        blue = num
        
        power = red * green * blue
        
        powers.append(power)
    
    return powers


games = {}

f = open("Game_data.txt", 'r')

for line in f:
    
    index_end_number = line.find(":")
    
    key = line[5:index_end_number]
    
    # format values into lists of lists
    value = str_to_list(line[index_end_number + 2: -1], ";")
    
    for i in range(len(value)):
        value[i] = str_to_list(value[i], ",")
    
    games[int(key)] = value

f.close()


# solution for puzzle 1
print(possible_games(games))

# solution for puzzle 2
powers_list = fewest_number(games)

sum_powers = 0

for i in powers_list:
    sum_powers += i
print(sum_powers)

