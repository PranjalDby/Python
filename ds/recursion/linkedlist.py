class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
def add_Head(head,data):
    if head is None:
        newnode = Node(data)
        newnode.next = head
        head = newnode
        return head
    
    newnode = Node(data)
    newnode.next = head
    head = newnode

    return head

def print_list(head):
    if head == None:
        return
    
    ptr = head
    print(ptr.data)
    print_list(ptr.next)

def reverse_list(head):
    if head == None or head.next == None:
        return head
    
    p = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return p

def merge_sorted(A,B):
    if A == None:
        return B
    
    if B == None:
        return A
    
    if A.data < B.data:
        A.next = merge_sorted(A.next,B)
        return A
    else:
        B.next = merge_sorted(A,B.next)
        return B


head1 = None
head1 = add_Head(head1,4)
head1 = add_Head(head1,3)
head1 = add_Head(head1,2)
head1 = add_Head(head1,1)
head2 = None
head2 = add_Head(head2,8)
head2 = add_Head(head2,7)
head2 = add_Head(head2,6)
head2 = add_Head(head2,5)

head3 = merge_sorted(head1,head2)
print_list(head3)
