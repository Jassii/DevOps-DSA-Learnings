class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = list()
        k=0
        for i in range(0,len(operations)):
            if(operations[i]=='C'):
                stack.pop()
                k-=1
            elif(operations[i]=='+'):
                summ = stack[k-1]+stack[k-2]
                stack.append(summ)
                k+=1
            elif(operations[i]=='D'):
                stack.append(stack[k-1]*2)
                k+=1
            else:
                stack.append(int(operations[i]))
                k+=1 #track the index of the stack
        
        return sum(stack)
