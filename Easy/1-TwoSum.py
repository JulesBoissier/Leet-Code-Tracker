from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {}

        for idx, num in enumerate(nums):

            if num in hm.keys():
                return [idx, hm[num]]

            else:
                hm[target - num] = idx
