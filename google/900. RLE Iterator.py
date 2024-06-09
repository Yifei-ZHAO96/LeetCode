from typing import List

class RLEIterator:

    # def __init__(self, encoding: List[int]):
    #     self.encoding = encoding
    #     self.idx = 0

    # # O(N)
    # def next(self, n: int) -> int:
    #     while self.idx < len(self.encoding):
    #         if self.encoding[self.idx] >= n:
    #             self.encoding[self.idx] -= n
    #             return self.encoding[self.idx + 1]
    #         else:
    #             n -= self.encoding[self.idx]
    #             self.idx += 2
        
    #     return -1

    # O(N) O(N)
    def __init__(self, encoding: List[int]):
        self.pre_sum_freq = []
        self.vals = []
        self.cur_sum = 0
        pre_sum = 0

        for i in range(0, len(encoding), 2):
            if encoding[i] != 0:
                pre_sum += encoding[i]
                self.pre_sum_freq.append(pre_sum)
                self.vals.append(encoding[i + 1])

    # O(logN) O(1)
    def next(self, n: int) -> int:
        self.cur_sum += n
        idx = self.bisect_left(self.pre_sum_freq, self.cur_sum)
        if idx == len(self.pre_sum_freq):
            return -1
        
        return self.vals[idx]
    
    def bisect_left(self, nums, n):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < n:
                l = m + 1
            else:
                r = m - 1

        return l
    
# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)