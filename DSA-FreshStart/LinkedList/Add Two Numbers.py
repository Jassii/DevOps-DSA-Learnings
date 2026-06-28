# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #now traverse both the linked lists and sum
        summ=0
        carry=0
        curr1=l1
        curr2=l2
        res=[]
        isThere=False
        while(curr1!=None and curr2!=None):
            summ = curr1.val + curr2.val + carry
            if(summ>9):
                rem=summ%10
                res.append(rem)
                carry = summ//10
                isThere=True
            else:
                res.append(summ)
                carry=0
                isThere=False
            
            curr1=curr1.next
            curr2=curr2.next


        while(curr1!=None):
            summ=0
            summ+=curr1.val+carry
            if(summ>9):
                rem=summ%10
                res.append(rem)
                carry=summ//10
                isThere=True
            else:
                res.append(summ)
                carry=0
                isThere=False
            curr1=curr1.next

        while(curr2!=None):
            summ=0
            summ+=curr2.val+carry
            if(summ>9):
                rem=summ%10
                res.append(rem)
                carry=summ//10
                isThere=True
            else:
                res.append(summ)
                carry=0
                isThere=False
            curr2=curr2.next 


        if(isThere==True):
            res.append(carry)
        
        #now the list contains the value
        head=ListNode(res[0])
        curr=head
        for i in range(1,len(res)):
            value=res[i]
            test=ListNode(value)
            curr.next=test
            curr=test
        
        #at last point the curr to None
        curr.next=None

        return head
