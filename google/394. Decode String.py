class Solution:
    # O(N) O(N)
    def decodeString(self, s: str) -> str:
        res = ''
        stack = []
        i = 0
        count = 0

        for i in range(len(s)):
            if s[i] == '[':
                stack.append((res, count))
                count = 0
                res = ''

            elif s[i] == ']':
                pre_res, count = stack.pop()
                res = pre_res + res * count
                count = 0
            
            elif s[i].isdigit():
                count = count * 10 + int(s[i])
            
            else:
                res += s[i]
            
        return res