import collections
from typing import List

class DetectSquares:

    def __init__(self):
        self.counter = collections.Counter()

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1

    # O(N)
    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for (i, j), freq in self.counter.items():
            if x == i or y == j or abs(x - i) != abs(y - j):
                continue
            res += freq * self.counter[(i, y)] * self.counter[(x, j)]
        
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)