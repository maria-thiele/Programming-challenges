"""
Solutions of the problem: 3. Longest Substring Without Repeating Characters (difficulty: medium)

The solution in the class Solution is the more efficient solution.
The alternative, less efficient solution is given below the Solution class.
"""

class Solution:
    # more efficient solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        uses dictionary to track characters already in the string
        1. loops through string until dublicate character is found
        2. checks if the current string is longer then the longest string found so far
            if yes, the current string becomes the longest string
        3. removes everything from the current string until the first instance of the dublicate
        4. starts at 1. again until no more characters in string
        """
        longest_substring = []
        current_substring = []
        used_characters = {}

        for i in range(len(s)):
            #print("Loop:", i)
            #print("Longest at the start:", longest_substring)
            #print("Dict at the start:", used_characters)
            #print("Current sub at the start:", current_substring)
            #print("Current:", s[i])
            if s[i] in used_characters:
                #print("Yes")
                if len(current_substring) > len(longest_substring):
                    #print("Current:", current_substring, "Longest:", longest_substring)
                    longest_substring = current_substring
                index = current_substring.index(s[i])
                for element in current_substring[:index]:
                    #print("Element:", element)
                    del used_characters[element]
                #print("Dict at the end:", used_characters)
                current_substring = current_substring[index+1 :]
                current_substring.append(s[i])
                #print("Current sub at the end:", current_substring)
            else:
                current_substring.append(s[i])
                used_characters[s[i]] = [i]
        if len(current_substring) > len(longest_substring):
            #print("Current:", current_substring, "Longest:", longest_substring)
            longest_substring = current_substring
        return len(longest_substring)
    

"""
Alternative solution
"""
# first solution
def lengthOfLongestSubstring_first(self, s: str) -> int:
    substrings = {}
    longest_substring = []
    starting_index = 0

    for i in range(len(s)):
        for key in list(substrings.keys()):
            if s[i] not in substrings[key] and substrings[key]:
                substrings[key].append(s[i])
            else:
                values = substrings[key]
                index = key
                substrings[key] = []
                del substrings[key]
                if len(longest_substring) < len(values):
                    longest_substring = values
                    starting_index = key
        substrings[i] = [s[i]]
        
    
    for key in substrings:
        values = substrings[key]
        index = key
        if len(longest_substring) < len(values):
            longest_substring = values
            starting_index = key

    return len(longest_substring)