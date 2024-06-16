from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, n in enumerate(nums):
            if n in lookup:
                return [lookup[n], i]
            else:
                lookup[target - n] = i
        
        return [-1, -1]