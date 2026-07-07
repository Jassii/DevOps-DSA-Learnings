# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #Brute force approach
        # listA=[]
        # listB=[]
        # currA=headA
        # currB=headB
        # while(currA!=None and currB!=None):
        #     listA.append(currA)
        #     listB.append(currB)
        #     currA=currA.next
        #     currB=currB.next
        
        # while(currA!=None):
        #     listA.append(currA)
        #     currA=currA.next
        
        # while(currB!=None):
        #     listB.append(currB)
        #     currB=currB.next
        

        # for i in range(0,len(listA)):
        #     if(listA[i] in listB):
        #         return listA[i]  
        # return None

        #little better approach
        #Using HashMap, and traversing only one LL : SC - O(N1)
        # hmap={}
        # currA=headA
        # while(currA!=None):
        #     hmap[currA]=1
        #     currA=currA.next
        
        # #now traverse another LL and check for each node if it is there in the HashMap
        # currB=headB
        # while(currB!=None):
        #     if(currB in hmap):
        #         return currB
        #     currB=currB.next
    
        # #if no intersection is there
        # return None


        #Optimized Approach
        #length of the first LL
        # n1=0
        # currA=headA
        # while(currA!=None):
        #     n1+=1
        #     currA=currA.next

        # #length of the second LL
        # n2=0
        # currB=headB
        # while(currB!=None):
        #     n2+=1
        #     currB=currB.next

        # #now check the difference and confirm the longest LL, and as per that move the pointer of the largest LL (both at the same position)
        # dif=0
        # currA=headA
        # currB=headB
        # if(n1>n2):
        #     dif=n1-n2
        #     while(dif>0 and currA!=None):
        #         currA=currA.next
        #         dif-=1
        # else:
        #     dif=n2-n1
        #     while(dif>0 and currB!=None):
        #         currB=currB.next
        #         dif-=1
        
        # #now currA and currB will be at the same position, traverse and check the same node (intersection point)
        # while(currA!=None and currB!=None):
        #     if(currA==currB):
        #         return currA
        #     currA=currA.next
        #     currB=currB.next

        # #no intersection point is there
        # return None


        #More Optimized Approach
        #if in both any one head is None, then there is no intersection
        if(headA==None or headB==None):
            return None

        temp1=headA
        temp2=headB
        while(temp1!=temp2):
            temp1=temp1.next
            temp2=temp2.next

            if(temp1==temp2):
                return temp1

            if(temp1==None):
                temp1=headB
            if(temp2==None):
                temp2=headA

        #comes out of the loop when both the node matches
        return temp1
