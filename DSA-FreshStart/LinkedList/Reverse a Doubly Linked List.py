"""
Structure of doubly linked list node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        curr=head
        prevn=None
        nextn=None
        while(curr!=None):
            nextn=curr.next
            curr.next=prevn
            curr.prev=nextn
            prevn=curr
            curr=nextn
        return prevn
