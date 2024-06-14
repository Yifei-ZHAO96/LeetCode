class Solution:
    def countTime(self, time: str) -> int:
        res = 1
        
        if time[4] == '?':
            res *= 10
        if time[3] == '?':
            res *= 6
        if time[:2] == '??':
            res *= 24
        elif time[1] == '?':
            res *= 10 if int(time[0]) < 2 else 4
        elif time[0] == '?':
            res *= 3 if int(time[1]) < 4 else 2
        
        return res