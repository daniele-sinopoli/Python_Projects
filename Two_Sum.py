"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

from os import name
from unittest.mock import numerics


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i,n_analizzato in enumerate(nums):
            complementare= target - n_analizzato

            for j in range(i+1, len(nums)):
                if nums[j] == complementare:
                    return [i, j]



if __name__=="__main__":
    solution=Solution()

    numbers=[2, 7, 11 ,15]
    target= 9

    result= solution.twoSum(numbers,target)
    print(result)


"""
versione O(n):

visited= {}

for i , num in enumerate(nums):
    complementare= target-num
    
    if complementare in visited:
        return [visited[complementare],i]
    visited[num]=i
"""





