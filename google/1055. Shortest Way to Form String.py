class Solution(object):
    # O(MN) O(1)
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        m, n = len(source), len(target)
        
        def longest_match(i, j):
            # O(M)
            while i < m and j < n:
                if source[i] == target[j]:
                    j += 1
                i += 1

            return j
        
        res, j = 0, 0
        
        # O(N)
        while j < n:
            match_idx = longest_match(0, j)
            if match_idx == j: # can not find the matched character
                return -1
        
            j = match_idx
            res += 1

        return res

source = "abc"
target = "abcbc"
print(Solution().shortestWay(source=source, target=target))
source = "abc"
target = "acdbc"
print(Solution().shortestWay(source=source, target=target))
source = "xyz"
target = "xzyxz"
print(Solution().shortestWay(source=source, target=target))