# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        #Brute force approach - TC:O(2N), SC:O(N)
        # odd=[]
        # even=[]
        # curr=head
        # count=1
        # while(curr!=None):
        #     if(count%2!=0):
        #         odd.append(curr.val)
        #     else:
        #         even.append(curr.val)
        #     curr=curr.next
        #     count+=1

        # #now traverse the odd list
        # curr=head
        # i=0
        # while(curr!=None and i<len(odd)):
        #     curr.val=odd[i]
        #     i+=1
        #     curr=curr.next
        
        # #now traverse the even list
        # i=0
        # while(curr!=None):
        #     curr.val=even[i]
        #     i+=1
        #     curr=curr.next
        
        # return head


        #Optimized Approach. - TC:O(n) and SC:O(1)

        #edge case
        # if(head==None or head.next==None):
        #     return head

        # ohead=head
        # ehead=head.next
        
        # tempOHead=ohead #track the odd position nodes
        # tempEHead=ehead #track the even position nodes
        
        # count=3
        # curr=ehead.next #it will track the whole LL
        # while(curr!=None):
        #     if(count%2!=0):
        #         #odd index
        #         tempOHead.next=curr
        #         tempOHead=tempOHead.next
        #     else:
        #         #even index
        #         tempEHead.next=curr
        #         tempEHead=tempEHead.next
        #     curr=curr.next
        #     count+=1
        
        # #now two LL is maintained odd and even,
        # tempOHead.next=ehead
        # tempEHead.next=None

        # return ohead

        #more better optimized approach
        if(head==None or head.next==None):
            return head
        
        evenStart = head.next
        odd=head
        even=evenStart
        while(even!=None and even.next!=None):
            odd.next = odd.next.next
            odd=odd.next
            even.next = even.next.next
            even=even.next
        
        odd.next = evenStart
        return head
