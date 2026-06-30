def deleteHead(head):
    #code here
    nextn=head.next
    nextn.prev=None
    head.next=None
    head=nextn
    return head
