# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Brute force approach - O(n) and sc - O(n)
        # arr=[]
        # curr=head
        # while(curr!=None):
        #     arr.append(curr.val)
        #     curr=curr.next
        
        # l=0
        # r=len(arr)-1
        # while(l<=r):
        #     if(arr[l]!=arr[r]):
        #         return False
        #     l+=1
        #     r-=1
        # return True

        #Optimized Approach
        #find the mid of the LL
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        
        #now from slow reverse the LL
        curr=slow
        prev=None
        nextn=None
        while(curr!=None):
            nextn=curr.next
            curr.next=prev
            prev=curr
            curr=nextn
        
        #prev will be the starting point of the second half of the LL
        curr=head
        while(prev!=None):
            if(curr.val!=prev.val):
                return False
            curr=curr.next
            prev=prev.next
        return True
