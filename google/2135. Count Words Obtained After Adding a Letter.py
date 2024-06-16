from typing import List

class Solution:
    # O(S+T) O(S)
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = set()

        # O(S) O(S)
        for word in startWords:
            m = 0
            for w in word:
                m ^= 1 << (ord(w) - ord('a'))
            seen.add(m)
        
        res = 0

        # O(T) O（1)
        for word in targetWords:
            m = 0
            for w in word:
                m ^= 1 << (ord(w) - ord('a'))
            
            for w in word:
                if m ^ 1 << (ord(w) - ord('a')) in seen:
                    res += 1
                    break
        
        return res
                