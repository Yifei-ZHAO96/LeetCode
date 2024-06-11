class Solution:
    # O(N logN) O(N) N = hi - lo + 1
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0}
        def getF(x):
            if x in memo:
                return memo[x]
            
            memo[x] = (getF(3 * x + 1) if x % 2 == 1 else getF(x // 2)) + 1
            return memo[x]

        ranges = list(range(lo, hi + 1))
        ranges.sort(key=lambda x: (getF(x), x))

        return ranges[k - 1]
