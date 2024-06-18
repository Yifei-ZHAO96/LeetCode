import collections

class Solution:
    # O(N logN) O(N)
    def countOfAtoms(self, formula: str) -> str:
        stack = [collections.Counter()]
        i = 0

        while i < len(formula):
            if formula[i] == '(':
                stack.append(collections.Counter())
                i += 1
            
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                
                freq = int(formula[i_start: i] or 1)

                for k, v in top.items():
                    stack[-1][k] += v * freq
            
            else:
                i_start = i
                i += 1

                while i < len(formula) and formula[i].islower():
                    i += 1
                
                s = formula[i_start: i]

                i_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                
                freq = int(formula[i_start: i] or 1)
                stack[-1][s] += freq
    
        res = ''
        for k in sorted(stack[-1].keys()):
            res += k
            if stack[-1][k] > 1:
                res += str(stack[-1][k])
        
        return res

        # return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else "") for name in sorted(stack[-1]))
