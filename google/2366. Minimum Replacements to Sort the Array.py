from typing import List
import math

class Solution:
    # O(N) O(1)
    def minimumReplacement(self, nums: List[int]) -> int:
        last = nums[-1]
        res = 0

        for i in range(len(nums)-2, -1, -1):
            if nums[i] > last:
                m = math.ceil(nums[i] / last) # number of parts
                res += m - 1 # m - 1 operations to get m parts
                last = nums[i] // m # the smallest remainder
            else:
                last = nums[i]

        return res
