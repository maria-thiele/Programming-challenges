"""
Solutions of the problem: 1. Two Sums (difficulty: easy)

The solution in the class Solution is the most efficient solution and produces the correct result in all test cases 
(test cases are provided by LeetCode).

The two alternative solutions (outside the class Solution) are either inefficient or only work in specific test cases.
"""
class Solution:
    
    # alternative that also works for negative elements in nums[]
    # has the best run time
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        finds the indices of the two integers that sum to a target
        uses a hashmap/dictionary as a basic structure

        Main idea: 
        loops through the dictionary once and stores each value as a key in a dictionary
        if the current number plus one of the keys adds to the target, the pair is found

        Dictionary structure:
        keys : int
            former elements from nums[]
        values : list[]
            first element is always the index of the key in nums[]
            if exists, the second element is the index of the element in nums[] that added to key sums to the target
        """
        possible_pairs = {} # dictionary storing possible pairs, keys -> integers, values -> indices of the values forming a pair

        for i in range(len(nums)):
            possible_key = target - nums[i]
            # keys = list(possible_pairs.keys())
            # print(possible_key, keys)

            if possible_key in possible_pairs:
                possible_pairs[possible_key].append(i)
                return possible_pairs[possible_key]
            else:
                possible_pairs[nums[i]] = [i]
        
        return []



"""
Alternative Solutions
"""
    
# basic solution (worst run time)
def twoSum_basic(self, nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                result.append(i)
                result.append(j)
                return result


# alternative solution (works only for positive nums[i])
def twoSum_alternative(self, nums: List[int], target: int) -> List[int]:
    possible_pairs = [] # stores tuples with (index_1, index_2, bool=False)
    target_half = target // 2
    result = []
    # print(target, target_half)
    
    for i in range(target_half + 1):
        possible_pairs.append([-1, -1, False])
    
    for index in range(len(nums)):
        if nums[index] > target:
            continue
        
        if nums[index] <= target_half:
            pair = possible_pairs[nums[index]]
        else:
            pair = possible_pairs[target - nums[index]]

        if pair[2] == False:
            pair[0] = index
            pair[2] = True
        else:
            pair[1] = index
            result.append(pair[0])
            result.append(pair[1])
            return result