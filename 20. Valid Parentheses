class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        diction = {'(':')', '{':'}', '[':']'}
        for ch in s:
            if ch in "({[":
                lst.append(ch)
            elif ch in ")}]":
                if len(lst) == 0:
                    return False
                
                elif diction[lst[-1]] != ch:
                    return False
                
                else:
                    lst.pop()
        
        return len(lst) == 0
