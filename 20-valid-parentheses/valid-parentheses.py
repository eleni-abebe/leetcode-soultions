class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        isbalanced=True
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in ')]}':
                if not stack:
                    isbalanced = False
                    break
                top = stack.pop()
                if (c == ')' and top != '(') or (c == ']' and top != '[') or (c == '}' and top != '{'):
                    isbalanced = False
                    break

        if stack:
            isbalanced = False

        return isbalanced

        

        