from typing import  List
import collections

class Solution:
    # O(N L**2 + N logN) O(NL)
    def longestStrChain(self, words: List[str]) -> int:
        # O(N logN) O(NL)
        words.sort(key=len)
        dp = collections.defaultdict(int) # the maximum len of the string chain ending with each word
        res = 1

        # O(N)
        for word in words:
            dp[word] = 1
            # O(L)
            for i in range(len(word)):
                # O(L) O(L)
                subword = word[:i] + word[i+1:]
                if subword in dp:
                    dp[word] = max(dp[word], 1 + dp[subword])
            
            res = max(res, dp[word])
        
        return res