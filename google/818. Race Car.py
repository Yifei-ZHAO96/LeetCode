from collections import deque

class Solution:
    # O(2**T) O(2**T) T: target
    def racecar(self, target: int) -> int:
        q = deque([(0, 1, 0)]) # moves, speed, location

        while q:
            move, speed, location = q.popleft()
            if location == target:
                return move
            
            # A
            q.append((move+1, speed * 2, location + speed))
            # wrong solution
            # if (location + speed <= target and speed > 0) or (location + speed >= target and speed < 0):
            #     q.append((move + 1, speed * 2, location + speed))
 
            # R
            if (location + speed > target and speed > 0) or (location + speed < target and speed < 0):
                q.append((move + 1, 1 if speed < 0 else -1, location))
        
        return -1