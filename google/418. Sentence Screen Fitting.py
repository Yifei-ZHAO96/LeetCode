from typing import List

class Solution:
    # O(RS) O(S)
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # O(S) O(S)
        sentence = ' '.join(sentence) + ' '
        cur = 0
        m = len(sentence)

        # O(R)
        for _ in range(rows):
            cur += cols
            if sentence[cur % m] == ' ':
                cur += 1

            # O(S)
            while cur and sentence[(cur - 1) % m] != ' ':
                cur -= 1

        return cur // m

sentence = ["hello","world"]
rows = 2
cols = 8
print(Solution().wordsTyping(sentence=sentence, rows=rows, cols=cols))

sentence = ["a", "bcd", "e"]
rows = 3
cols = 6
print(Solution().wordsTyping(sentence=sentence, rows=rows, cols=cols))

sentence = ["i","had","apple","pie"]
rows = 4
cols = 5
print(Solution().wordsTyping(sentence=sentence, rows=rows, cols=cols))