from typing import List

class Solution:
    # O(MNW) O(MN + W)
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        # O(W) O(W)
        words = [word, word[::-1]]
        # O(1)
        for matrix in [board, list(zip(*board))]: # transpose, O(MN) O(MN)
            # O(1)
            for w in words:
                # O(M)
                for row in matrix:
                    # O(N)
                    for block in ''.join(row).split('#'):
                        # O(W)
                        if len(block) == len(word) and all(w[i] == block[i] or block[i] == ' ' for i in range(len(word))):
                            return True
        
        return False


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
word = "abc"
print(board)
print(list(zip(*board)))