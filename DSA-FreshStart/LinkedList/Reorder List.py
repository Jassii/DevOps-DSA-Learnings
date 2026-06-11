# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find the mid of the linked list
        slow=head
        fast=head.next
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        
        #now next node of the slow node will be the head of the another linked list
        second=slow.next
        slow.next=None #why this because we will be splitting the single list into two single linked list
        
        #now reverse the another linked list
        prev=None
        curr=second
        nextn=None
        while(curr!=None):
            nextn=curr.next
            curr.next=prev
            prev=curr
            curr=nextn
        
        #now traverse both the linked list and pick one by one and merge the LL.
        curr1=head
        curr2=prev #head of the second linked list
        while(curr2!=None):
            temp1,temp2=curr1.next,curr2.next
            curr1.next=curr2
            curr2.next=temp1
            curr1=temp1
            curr2=temp2
        
        return head
