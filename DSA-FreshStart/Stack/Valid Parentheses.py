class Solution:
    def isValid(self, s: str) -> bool:
        stack=list()
        for i in range(0,len(s)):
            ch=s[i]
            if(ch=='(' or ch=='[' or ch=='{'):
                stack.append(ch)
            elif(ch==')'):
                if(len(stack)>0 and stack[len(stack)-1]=='('):
                    stack.pop(len(stack)-1)
                else:
                    return False
            elif(ch==']'):
                if(len(stack)>0 and stack[len(stack)-1]=='['):
                    stack.pop(len(stack)-1)
                else:
                    return False
            elif(ch=='}'):
                if(len(stack)>0 and stack[len(stack)-1]=='{'):
                    stack.pop(len(stack)-1)
                else:
                    return False
        
        if (len(stack)==0):
            return True

        return False
