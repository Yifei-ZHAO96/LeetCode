class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(minute, sec):
            s, cur, res = str(minute * 100 + sec), str(startAt), 0

            for c in s:
                if c == cur:
                    res += pushCost
                else:
                    res += pushCost + moveCost
                    cur = c
            
            return res
        
        minutes = targetSeconds // 60
        res = float('inf')

        for minute in range(minutes + 1):
            if minute > 99:
                break
            second = targetSeconds - minute * 60
            if second > 99:
                continue
            
            res = min(res, cost(minute, second))

        return res