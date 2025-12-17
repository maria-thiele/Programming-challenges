#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:26:12 2023

@author: maria
"""
"""
Day 1 :
    The tasks were to compute the sum of all calibration numbers.
    The calibration numbers are stored in a text file called Calibration_data.txt
    These numbers were in the form of letters mixed with numbers: e.g. frone6sevenine67three
    The function get_calibration_problem1 searches for the first and last digit (1, 2,...).
    The corresponding calibration number is a two digit number, of the first found digit and the last found digit.
    Since some digits are written as words, the function get_calibration_problem2 does the same 
    but with respect to the wordly written numbers.

Remark :
    The documentation was last changed on the 6.12.2023
    It is supposed to help understand the code but might lack some coherence and detail.

This code produced the correct answers.
"""
import io


data = []

# read the clibration data into a list
f = io.open("Calibration_data.txt", 'r')

for line in f:
    modified_data = line[0:-1]
    data.append(modified_data)

f.close()

#print(data)



numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
word_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def get_calibration_problem1(data : list[str]):
    """
    for every element of the list data, the function gets the first and last occurance of a number in the string
    it then stores those numbers in a new list
    Finally those numbers are added together

    Returns
    -------
    result : int
        Sum of all the numbers in calibration_numbers.

    """
    calibration_numbers = []
    
    for element in data:
        num1 = 0
        num2 = 0
        for i in range(len(element)):
            if element[i] in numbers:
                num1 = element[i]
                break
        for i in range(len(element)):
            if element[len(element)-1 - i] in numbers:
                num2 = element[len(element) - 1 - i]
                break
        
        number = num1 + num2
        calibration_numbers.append(int(number))
    
    #print(calibration_numbers)
    
    result = 0
    
    for i in calibration_numbers:
        result += i
    
    return result


def get_calibration_problem2(data : list[str]):
    """
    The list data contains string elements. Every element is made up of letters and numbers.
    This function takes the first and last digit, puts them together as a whole number and stores them in the list calibration_numbers.
    Thereby, it does not matter whether digits are in form of digits (e.g 1, 2, etc) or as words (e.g. one, two, etc...).
    The function returns the sum of all the numbers in calibration_numbers

    Parameters
    ----------
    data : list[str]
        list of strings made up of letters and digits.

    Returns
    -------
    result : int
        sum of the elements of calibration_list.
    """
    
    calibration_numbers = []
    
    for element in data:
        num1 = 0
        num2 = 0
        index_first = 0
        index_last = 0
        
        
        # search for the first and last occurance of a digit (e.g 1, 2,...)
        for i in range(len(element)):
            if element[i] in numbers:
                num1 = element[i]
                index_first = i
                break
        for i in range(len(element)):
            if element[len(element)-1 - i] in numbers:
                num2 = element[len(element) - 1 - i]
                index_last = len(element) - 1 - i
                break
        
        # search for substrings of the "word-digits" (one, two,...)
        # if a word digit occurs before/after the first/last digit, the indices are changed accordingly
        for index in range(len(word_numbers)):
            word_index = element.find(word_numbers[index])
            
            if word_index != -1:
                if word_index < index_first:
                    index_first = word_index
                    num1 = str(index)
        
        for index in range(len(word_numbers)):
            word_index = element.rfind(word_numbers[index])
            
            if word_index != -1:
                if word_index > index_last:
                    index_last = word_index
                    num2 = str(index)
        
        # compute the sum of all the numbers
        
        number = num1 + num2
        calibration_numbers.append(int(number))
        
    result = 0
    
    for i in calibration_numbers:
        result += i
    
    return result


print(get_calibration_problem1(data))
print(get_calibration_problem2(data))

#test_data = ['5gstwoone67oneight']
#print(get_calibration_problem2(test_data))
