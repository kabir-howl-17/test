class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

head = Node(5)
print(head.data)
print(head.next)
head.next = Node(6)
head.next.next = Node(7)
print(head.next.data)
print(head.next.next.data)
