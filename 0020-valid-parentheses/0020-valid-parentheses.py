class Solution(object):
    def isValid(self, s):
        stack = []
        openBrackets = {'[', '{', '('}
        closeBrackets = {']', '}', ')'}
        for i in s:
            if i in openBrackets:
                stack.append(i)
            elif i in closeBrackets and len(stack) != 0:
                if i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) != 0:
            return False
        return True
        