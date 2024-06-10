from typing import List


class Solution:
    # O(sqrt N)
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        res = []
        if finalSum % 2:
            return res
        
        i = 2
        while i <= finalSum:
            finalSum -= i
            res.append(i)
            i += 2
        res[-1] += finalSum

        return res