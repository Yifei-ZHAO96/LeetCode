from typing import List
import heapq

# 定义 Interval 类
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'Interval({self.start}, {self.end})'
    

class Solution:
    # N: number of employee, M: number of schedules
    # O(M logN) O(N)
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        result = []
        # start, employee_id, idx
        min_heap = [(sch[0].start, e_id, 0) for e_id, sch in enumerate(schedule)]
        heapq.heapify(min_heap)
        last_end = -1
        
        
        while min_heap:
            # O(logN)
            s, id, i = heapq.heappop(min_heap)
            if 0 <= last_end < s:
                result.append(Interval(last_end, s))
            
            last_end = max(last_end, schedule[id][i].end)
            if i + 1 < len(schedule[id]):
                heapq.heappush(min_heap, (schedule[id][i+1].start, id, i+1))
        
        return result

# 示例输入
schedule = [
    [Interval(1, 2), Interval(5, 6)],
    [Interval(1, 3)],
    [Interval(4, 10)]
]

# 创建 Solution 实例并调用 employeeFreeTime 方法
sol = Solution()
print(sol.employeeFreeTime(schedule))  # 输出应为 [Interval(3, 4)]

schedule = [
    [Interval(1,3), Interval(6,7)],
    [Interval(2,4)],
    [Interval(2,5)],
    [Interval(9,12)]
    ]
print(sol.employeeFreeTime(schedule))  # 输出应为 [Interval(3, 4)]
