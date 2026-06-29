''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        # code here
        if(head==None):
            return 0
        
        curr=head
        count=0
        while(curr!=None):
            count+=1
            curr=curr.next
        
        return count
