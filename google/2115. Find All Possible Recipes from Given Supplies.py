import collections
from typing import List

class Solution:
    # Topo sort
    # O(NM + S) O(NM + S)
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)

        # O(NM) O(NM)
        for recepie, ingredient in zip(recipes, ingredients):
            for i in ingredient:
                graph[i].append(recepie)
                in_degree[recepie] += 1
        
        res = []
        # O(S) O(S)
        q = collections.deque(supplies)

        # O(NM)
        while q:
            len_q = len(q)
            for _ in range(len_q):
                sup = q.popleft()
                
                for r in graph[sup]:
                    in_degree[r] -= 1
                    if in_degree[r] == 0:
                        res.append(r)
                        q.append(r)
        
        return res