from typing import List
import random


class Solution:

    # O(N) O(N)
    def __init__(self, w: List[int]):
        self.weight = []
        pre_sum = 0

        for n in w:
            pre_sum += n
            self.weight.append(pre_sum)

    # O(logN) O(1)
    def pickIndex(self) -> int:
        target = random.random() * self.weight[-1]
        l, r = 0, len(self.weight) - 1

        while l <= r:
            m = (l + r) // 2
            if self.weight[m] < target:
                l = m + 1
            elif self.weight[m] > target:
                r = m - 1
            else:
                return m
        
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()