from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1 and abs(cards[0] - 24) <= 0.001:
            return True
        
        for i in range(len(cards) - 1):
            for j in range(i+1, len(cards)):
                base = [cards[k] for k in range(len(cards)) if k != i and k != j]
                if self.judgePoint24(base + [cards[i] + cards[j]]): return True
                if self.judgePoint24(base + [cards[i] - cards[j]]): return True
                if self.judgePoint24(base + [cards[j] - cards[i]]): return True
                if self.judgePoint24(base + [cards[i] * cards[j]]): return True
                if cards[j] != 0 and self.judgePoint24(base + [cards[i] / cards[j]]): return True
                if cards[i] != 0 and self.judgePoint24(base + [cards[j] / cards[i]]): return True
        
        return False