from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        
        #Brute force Approach
        # res=[]
        # if(head==None or head.next==None):
        #     return res
        
        # i=head
        # while(i!=None):
        #     j=i.next
        #     while(j!=None):
        #         if((i.data+j.data)==target):
        #             lis=[]
        #             lis.append(i.data)
        #             lis.append(j.data)
        #             res.append(lis)
        #         j=j.next
        #     i=i.next
        # return res
        
        #result
        res=[]
        
        #reach to the last node
        curr=head
        while(curr.next!=None):
            curr=curr.next
        
        #as the DLL is in sorted order, hence you can use two pointer approach
        #last node
        end=curr
        #starting node
        start=head
        while(start.data<end.data):
            if((start.data+end.data)>target):
                end=end.prev
            elif((start.data+end.data)<target):
                start=start.next
            else:
                lis=[]
                lis.append(start.data)
                lis.append(end.data)
                res.append(lis)
                start=start.next
                end=end.prev
        
        return res
