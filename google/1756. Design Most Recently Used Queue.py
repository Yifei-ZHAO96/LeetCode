from collections import deque
import math

class MRUQueue:
    # O(N)
    def __init__(self, n: int):
        self.block_size = int(math.sqrt(n)) + 1
        self.block = [deque() for _ in range(self.block_size)]
        
        for i in range(n):
            self.block[i // self.block_size].append(i + 1)
    
    # O(sqrt(N))
    def fetch(self, k: int) -> int:
        k -= 1
        block_id = k // self.block_size
        idx = k % self.block_size
        val = self.block[block_id][idx]
        self.block[-1].append(val)

        del self.block[block_id][idx]
        
        for i in range(block_id, self.block_size - 1):
            self.block[i].append(self.block[i+1].popleft())
        
        return val

mru_queue = MRUQueue(8)
print(mru_queue.fetch(3))  # Output: 3
print(mru_queue.fetch(5))  # Output: 6
print(mru_queue.fetch(2))  # Output: 2
print(mru_queue.fetch(8))  # Output: 2