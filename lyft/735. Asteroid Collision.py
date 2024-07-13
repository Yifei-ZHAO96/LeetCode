from typing import List

class Solution:
    # O(N) O(N)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] + a < 0:
                    stack.pop()
                elif stack[-1] + a == 0:
                    stack.pop()
                    break
                else:
                    break
            
            else:
                stack.append(a)
        
        return stack