class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {']':'[', '}' : '{', ')' : '('}
        for i in s:
            if i in mapping:
                top_stack = stack.pop() if stack else '#'
                if top_stack != mapping[i]:
                    return False
            else:
                stack.append(i)
        return not stack
        