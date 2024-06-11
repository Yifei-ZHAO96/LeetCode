from typing import List


class Solution:
    # O(N logN) O(N)
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        max_def = 0
        res = 0

        for _, def_ in properties:
            if max_def > def_:
                res += 1
            
            max_def = max(max_def, def_)

        return res