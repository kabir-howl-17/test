class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
def printList(head):
    cur = head
    while cur!=None:
        print(cur.data, end = " ")
        cur = cur.next
new_head = None
def reverse_LL_rec(head,prev):
    global new_head
    if head is None:
        return
    if head.next is None:
        head.next = prev
        return head
    new_head = reverse_LL_rec(head.next,head)
    head.next = prev
    return new_head
if __name__ == "__main__":
    head = Node(5)
    head.next = Node(15)
    head.next.next = Node(25)
    head.next.next.next = Node(35)
    printList(head)
    print()
    head_rev = reverse_LL_rec(head,None)
    printList(head_rev)
    print()
