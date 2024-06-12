from typing import List

class Solution:
    # O(N) O(N)
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def blank(n):
            return ' ' * n
        
        res = []
        r = 0

        while True:
            l = r
            cur_word_len = 0

            while r < len(words) and cur_word_len + len(words[r]) + r - l <= maxWidth:
                cur_word_len += len(words[r])
                r += 1
            
            # last line
            if r == len(words):
                s = ' '.join(words[l: r])
                s += blank(maxWidth - len(s))
                res.append(s)
                break
            
            num_words = r - l
            num_space = maxWidth - cur_word_len

            # only 1 word
            if num_words == 1:
                s = words[l] + blank(maxWidth - len(words[l]))
                res.append(s)
                continue
            
            # other scenarios
            avg = num_space // (num_words - 1)
            extra = num_space % (num_words - 1) # extra spaces inserted to the left
            # Join the first extra+1 words with an extra space, and the remaining words with average spaces
            s = blank(avg + 1).join(words[l: l + extra + 1]) + \
                blank(avg) + \
                blank(avg).join(words[l + extra + 1: r])
            res.append(s)
        
        return res