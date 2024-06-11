class Solution:
    # O(N) O(1)
    def canTransform(self, start: str, end: str) -> bool:
        if start.count('X') != end.count('X'):
            return False
        
        n = len(start)
        i = j = 0

        while i < n and j < n:
            if start[i] == 'X':
                i += 1
                continue
            if end[j] == 'X':
                j += 1
                continue
            
            if start[i] != end[j]: return False
            if start[i] == 'R' and i > j: return False
            if start[i] == 'L' and i < j: return False
            i += 1
            j += 1
        
        return True