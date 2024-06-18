from typing import List
import collections

class Solution:
    # O(S + WM) O(WM), W = len(words) M = avg(len(word))
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        heads = collections.defaultdict(list)
        # O(W) O(W)
        for i in range(len(words)):
            heads[words[i][0]].append((i, 0)) # i-th word, j-th character

        res = 0

        # O(S + WM) O(WM) W = len(words) M = avg(len(word))
        for c in s:
            matches = heads[c]
            heads[c] = [] # c is visited and will no longer be used, instead to save the new matches

            for i, j in matches:
                j += 1 # 
                if j == len(words[i]):
                    res += 1
                
                else:
                    heads[words[i][j]].append((i, j)) # match for the next character

        return res