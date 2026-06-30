'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        # Code Here
        count=0
        curr=head
        new_node = Node(x)
        while(curr!=None):
            if(count==p):
                if(curr.next!=None):
                    nextn=curr.next
                    curr.next=new_node
                    new_node.prev=curr
                    new_node.next=nextn
                    nextn.prev=new_node
                    break
                else:
                    curr.next=new_node
                    new_node.prev=curr
                    break
            curr=curr.next
            count+=1
        return head
