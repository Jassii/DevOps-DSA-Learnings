# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #initialize the head of the merged linked list
        head=ListNode(-1)

        curr1,curr2=list1,list2

        if(curr1==None and curr2==None):
            return None
        elif(curr1==None and curr2!=None):
            return curr2
        elif(curr1!=None and curr2==None):
            return curr1

        #first decide the head of the merged linked list
        if(curr1.val<=curr2.val):
            head=curr1
            curr1=curr1.next
        elif(curr2.val<curr1.val):
            head=curr2
            curr2=curr2.next
        
        temp=head
        while(curr1!=None and curr2!=None):
            if(curr1.val<=curr2.val):
                temp.next=curr1
                curr1=curr1.next
            else:
                temp.next=curr2
                curr2=curr2.next
            temp=temp.next

        while(curr1!=None):
            temp.next=curr1
            curr1=curr1.next
            temp=temp.next
        
        while(curr2!=None):
            temp.next=curr2
            curr2=curr2.next
            temp=temp.next
        
        return head
