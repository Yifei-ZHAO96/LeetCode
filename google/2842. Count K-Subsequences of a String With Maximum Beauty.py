from collections import Counter
from typing import List
from math import comb

class Solution:
    # O(S logS) O(S)
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        mod = 10 ** 9 + 7
        counter = Counter(s)
        if len(counter) < k:
            return 0

        freq = Counter(counter.values())
        pairs = list(sorted(freq.items(), reverse=True))
        res = 1

        for fc, occ in pairs:
            if occ <= k:
                res = (res * pow(fc, occ, mod)) % mod
                k -= occ
            else:
                res = (res * comb(occ, k) * pow(fc, k, mod)) % mod
                break
        
        return res % mod