"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.
"""

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        tmp_list = []
        for i in range(0, len(nums), 2):
            tmp_list += ([nums[i + 1] for _ in range(nums[i])])
        return tmp_list
