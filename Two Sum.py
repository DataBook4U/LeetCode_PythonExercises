"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

"""

class solution():

    def __init__(self, nums: list[int], target: int):
        self.nums = nums
        self.target = target

    def result(self):
        iter1 = 0
        iter2 = 1
        stop = len(self.nums)
        self.resultList = []
        while iter2 < stop:
            r = self.nums[iter1] + self.nums[iter2]
            if r == self.target:
                self.resultList.append(iter1)
                self.resultList.append(iter2)
            iter1 += 1
            iter2 += 1
        return self.resultList


run1 = solution(nums = [3,3], target = 6)
run1.result()

#Accepted LeetCode Version:

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iter1 = 0
        iter2 = 1
        stop = len(nums)
        resultList = []
        while iter2 < stop:
            r = nums[iter1] + nums[iter2]
            if r == target:
                resultList.append(iter1)
                resultList.append(iter2)
            iter1 += 1
            iter2 += 1
        return resultList
"""