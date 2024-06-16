from typing import List
import heapq

class Solution:
    # O(NlogN) O(N)
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((e, i, p) for i, (e, p) in enumerate(tasks))
        res = []
        q = [] # (enque_time, task_id)
        start_Time = tasks[0][0]
        i = 0

        while len(res) < len(tasks):

            while i < len(tasks) and tasks[i][0] <= start_Time:
                heapq.heappush(q, (tasks[i][2], tasks[i][1]))
                i += 1

            if q:
                p, j = heapq.heappop(q)
                res.append(j)
                start_Time += p
            
            elif i < len(tasks):
                start_Time = tasks[i][0]

        return res