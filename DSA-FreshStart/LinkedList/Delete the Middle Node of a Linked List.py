# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #only one node is there
        if(head.next==None):
            return None

        prev=None
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            prev=slow
            slow=slow.next
            fast=fast.next.next
        
        #slow will be at the middle of the ll and prev will be the just before node of the slow/middle node
        #remove the middle node
        prev.next=slow.next
        slow.next=None

        return head
