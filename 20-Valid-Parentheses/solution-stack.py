class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {')':'(',']':'[','}':'{'}
        for c in s:
            if c in match:
                if not(stack and stack.pop()==match[c]):
                    return False
            else:
                stack.append(c)
        return not stack
#learned from bbs
            
