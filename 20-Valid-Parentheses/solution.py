class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        elif len(s)%2!=0:
            return False
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('[]','').replace('()','')
        if len(s)==0:
            return True
        else:
            return False
#learned from bbs tricky
            
