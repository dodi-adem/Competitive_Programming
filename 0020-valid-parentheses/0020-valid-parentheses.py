class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapping = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        if s[0] in mapping.keys():
            return False
        
        
        for char in s:
            if char in mapping.values():
                stk.append(char)
            else:
                if stk and stk[-1] == mapping[char]:
                    stk.pop()
                else:
                    stk.append(char)
        return not stk
        