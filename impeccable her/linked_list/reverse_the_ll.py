class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


head = None


head = Node(28)
head.next = Node(10)
head.next.next = Node(62)
head.next.next.next = Node(17)


def printplea(head):
    cur = head
    while cur != None:
        print(cur.data, end = " ")
        cur = cur.next

def reversee(head):
    pre = None
    cur = head
    while cur != None:
        nxt = cur.next

        cur.next = pre
        pre = cur 
        cur = nxt
    head = pre
    return head



blue = reversee(head)
printplea(blue)
