#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 01:07:29 2023

@author: maria
"""

"""
Day 4 :
    The tasks were based on a game of cards where each card had winning numbers and drawn numbers.
    
    In the first task, every drawn number that matched a winning number gave points. 
    The first matching number gave one point and every matching number after doubled the points.
    The total number of points was the result.
    
    In the second task, matching numbers produced copies of the following cards.
    If one card has two matching numbers, the following two cards received one copie.
    Every copie counts as an instance of a card and is counted as a normal card.
    If a card has two copies, and those copies have one matching number, the following card receives two copies.
    The result is the total amount of cards (originals and copies)

Remark :
    The documentation was last changed on the 20.12.2023
    It is supposed to help understand the code but might lack some coherence and detail.

This code produced the correct answers.
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


def str_to_list(string : str):
    """
    Converts a given string into a list.
    The input string contains numbers (maximum two digits) that are seperated by a single space.
    If a number only has one digit, there is an additional space in front of the digit.
    The list takes all the numnbers of the string and ignores the spaces that do not belong to a one digit number

    Parameters
    ----------
    string : str
        A string containing two or one digit numbers.
        The numbers are seperated by a single space.
        Every number has two places: for two digit numbers those are two digits, 
        for a one digit number it is a space followed by the digit.

    Returns
    -------
    llist : list[str]
        list containing all the numbers as elements
        The numbers are still of type string and one digit numbers are strings with one space and than the digit.
    """
    
    llist = []
    
    
    while len(string) > 2:
        
        llist.append(string[0:2])
        string = string[3:]
    
    llist.append(string)
    
    return llist


def format_data(line : str):
    """
    Seperates the winning numbers and the drawn numbers in the given string from one another.
    The information about the game is ignored.

    Parameters
    ----------
    line : str
        input data: a string with the game number, the winning numbers and the drawn numbers.
        The format is game : winning numbers | drawn numbers

    Returns
    -------
    numbers : list[str]
        a list where the first element is the string containing the winning numbers 
        and the second element is a string containing the drawn numbers

    """
    
    winning_nums = ""
    drawn_nums = ""
    
    colon_index = line.find(":")
    line = line[colon_index + 2:]
    seperater_index = line.find("|")
    
    winning_nums = line[:seperater_index - 1]
    drawn_nums = line[seperater_index + 2:]
    
    numbers = [winning_nums, drawn_nums]
    
    return numbers


def count_winnings(wins : list[str], draws : list[str]):
    """
    Counts the total number of matching numbers

    Parameters
    ----------
    wins : list[str]
        the winning numbers
    draws : list[str]
        the drawn numbers

    Returns
    -------
    counter : int
        amount of matching drawn numbers with winning numbers

    """
    
    counter = 0
    
    for num in wins:
        if num in draws:
            counter += 1
    
    return counter



def make_dict(data : list):
    """
    Creates a dictionary with integer values as keys and the number 1 has the default value

    Parameters
    ----------
    data : list
        length of the list indicates the number of cards

    Returns
    -------
    new_dict : dict
        dictionary with the card number as key and the default value 1 

    """
    
    new_dict = {}
    
    for i in range(len(data)):
        new_dict[i+1] = 1
    
    return new_dict


################# read data ####################

data = read_data("Card_data.txt")
#print(data)



################# Task 1 #######################

winnings = []

for i in data:
    
    # compute the number of winning numbers
    info = format_data(i)
    wins = str_to_list(info[0])
    draws = str_to_list(info[1])
    
    amount = count_winnings(wins, draws)
    
    # compute the points that the winning number of winning numbers give
    if amount != 0:
        winning = 2**(amount - 1)
        winnings.append(winning)

# sum the winnings of each card
s = 0
for i in winnings:
    s += i

print(s)




################# Task 2 #######################

cards = make_dict(data)
print(cards)

total_cards = 0

for i in range(1, len(data)+1):
    
    # count the number of winning numbers
    info = format_data(data[i-1])
    wins = str_to_list(info[0])
    draws = str_to_list(info[1])
    
    copies = count_winnings(wins, draws)
    
    # for every (copie) card, evealuate the copies of the following cards
    for count in range(cards[i]):
        
        # increase the copie counter by one for every card in the given range
        for j in range(1, copies + 1):
            try:
                cards[i+j] += 1
            except:
                break
    
    # count the total number of cards
    total_cards += cards[i]

print(cards)

print(total_cards)




















