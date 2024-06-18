from typing import List

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        seen = set()
        
        for word in dict:
            
            for i in range(len(word)):
                t = word[:i] + '*' + word[i+1:]
                
                if t in seen:
                    return True
                seen.add(t)
        
        return False