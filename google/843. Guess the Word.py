import random
from typing import List

class Master:
    def guess(self, word: str) -> int:
        pass

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        times = 0
        x = 0 

        while times < 10 and x != 6:
            idx = random.randint(0, len(words) - 1)
            word = words[idx]

            x = master.guess(word)
            candidates = []
            for candidate in words:
                if x == self.match(word, candidate):
                    candidates.append(candidate)
                
            words = candidates
        
        return word

    def match(self, x, y):
        res = 0
        for i in range(len(x)):
            if x[i] == y[i]:
                res += 1
        
        return res