class Solution(object):
    def isValid(self, s):
        stack = []

        for i in range(len(s)):
            if(s[i] == ')' or s[i] == '}' or s[i] == ']'):
                if(len(stack) == 0):
                    return False

                elif((s[i] == ')' and stack[-1] == '(') or (s[i] == '}' and stack[-1] == '{') or (s[i] == ']' and stack[-1] == '[')):
                    stack.pop()
                else:
                    return False

            else:
                stack.append(s[i])

        if(len(stack) != 0):
            return False
        else:
            return True
        
            
        
