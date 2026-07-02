'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow=head
        fast=head
        #check if there is a loop in the LL
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                #loop exists
                count=1
                while(slow.next!=fast):
                    count+=1
                    slow=slow.next
                #count will be the length of the LL
                return count
        
        #no loop is found in the LL
        return 0
