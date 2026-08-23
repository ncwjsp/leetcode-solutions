class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if stack and stack[-1] + i in ("()", "[]", "{}"):
                stack.pop()
            else:
                stack.append(i)

        if stack:
            return False
        else:
            return True
                
                
        