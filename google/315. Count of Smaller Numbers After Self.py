from typing import List

class Solution:
    # O(NlogN) O(N)
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)
        enums = list(enumerate(nums))
        
        def mergesort(enums):
            half = len(enums) // 2
            if not half:
                return enums
            
            left, right = map(mergesort, (enums[:half], enums[half:]))
            
            for i in range(len(enums)-1, -1, -1):
                if not right or left and left[-1][1] > right[-1][1]:
                    res[left[-1][0]] += len(right)
                    enums[i] = left.pop()
                
                else:
                    enums[i] = right.pop()
            
            return enums

        mergesort(enums)
        
        return res