class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

def merge(head1,head2):
    head3 = None
    
    p1 = head1
    p2 = head2

    while p1 != None and p2 != None:
        if p1.data < p2.data:
            if head3 == None:
                head3 = Node(p1.data)
                cur = head3
            else:
                cur.next = Node(p1.data)
                cur = cur.next
            p1 = p1.next
        else:
            if head3 == None:
                head3 = Node(p2.data)
                cur = head3
            else:
                cur.next = Node(p2.data)
                cur = cur.next
            p2 = p2.next

    while p1 != None:
        cur.next = Node(p1.data)
        cur = cur.next
        p1 = p1.next
    while p2 != None:
        cur.next = Node(p2.data)
        cur = cur.next
        p2 = p2.next

    return head3

def printit(head):
    cur = head
    while cur != None:
        print(cur.data, end = " ")
        cur = cur.next

head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(8)


#driver code

aainu =  merge(head1,head2)
printit(aainu)
