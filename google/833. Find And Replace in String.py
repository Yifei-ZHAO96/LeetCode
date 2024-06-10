from typing import List

class Solution:
    # O(MK + S) O(S + MK)
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replace = [(c, 1) for c in s] # O(S) O(S)

        for i, sou, tar in zip(indices, sources, targets): # O(M)
            if s.startswith(sou, i): # O(K)
                replace[i] = (tar, len(sou)) # O(1) O(MK)

        res = ''
        i = 0
        while i < len(s): # O(S)
            res += replace[i][0]
            i += replace[i][1]
        
        return res