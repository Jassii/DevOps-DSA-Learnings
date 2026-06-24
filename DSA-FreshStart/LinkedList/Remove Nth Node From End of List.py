# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #count total nodes of the linked list
        count=1
        curr=head
        while(curr.next!=None):
            count+=1
            curr=curr.next
        

        nthNode=count-n+1
        if(nthNode==1):
            head=head.next
            return head


        prev=None
        curr=head
        k=1
        while(curr!=None):
            if(k==nthNode):
                curr=curr.next
                prev.next=curr
                break
            else:
                prev=curr
                curr=curr.next
                k+=1
        
        return head
