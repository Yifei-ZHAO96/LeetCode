from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 == p3 == p4:
            return False
        
        points = [p1, p2, p3, p4]
        points.sort()
        p1, p2, p3, p4 = points

        def distance(x, y):
            return (y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2
        
        d1 = distance(p1, p2)
        d2 = distance(p1, p3)
        d3 = distance(p1, p4)
        d4 = distance(p4, p2)
        d5 = distance(p4, p3)

        if not (d1 == d2 == d4 == d5):
            return False
        
        if not (d1 + d2 == d3 == d4 + d5):
            return False
        
        return True