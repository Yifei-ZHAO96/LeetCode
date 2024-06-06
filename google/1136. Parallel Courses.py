from typing import List
from collections import defaultdict, deque

class Solution:
    # O(N + M) O(N + M)
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_degree = [0] * n

        # O(M)
        for pre, next_ in relations:
            graph[pre - 1].append(next_ - 1)
            in_degree[next_ - 1] += 1
        
        res = 0
        course = deque([])
        
        # O(N)
        for i in range(n):
            if in_degree[i] == 0:
                course.append(i)
        
        # O(N)
        while course:
            len_course = len(course)
            res += 1
            
            for _ in range(len_course):
                pre = course.popleft()
                n -= 1

                for next_ in graph[pre]:
                    in_degree[next_] -= 1
                    
                    if in_degree[next_] == 0:
                        course.append(next_)
        
        return -1 if n else res

n = 3
relations = [[1,3],[2,3]]
sol = Solution()
print(sol.minimumSemesters(n, relations))