"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = max(nums)
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            if tmp >= 0:
                max_num = max(max_num, tmp)
            else:
                tmp = 0
        return max_num
