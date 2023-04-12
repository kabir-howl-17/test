class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


head = None

#function to add a new node at the end of linked list
def add_node_at_end(x):
    global head

    if head == None:
        head = Node(x)
        return
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(x)

#function to print the whole linked list 
def print_linked_list():
    global head

    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

#add at beginning of linked list
def add_at_beginning(x):
    global head
    if head == None:
        head = Node(x)
        return
    blue = Node(x)
    blue.next = head
    head = blue


#function to add a node at desired position in linked list

def add_at_desired_position(k,x):
    global head
    if head == None:
        head = Node(x)
        return
    curr = head
    count = 1
    while count < k-1:
        curr = curr.next
        count = count + 1

    newbud = Node(x)
    newbud.next = curr.next
    curr.next = newbud

#driver code
add_node_at_end(17)
add_node_at_end(62)
print_linked_list()
add_node_at_end(28)
add_node_at_end(23)
print_linked_list()
add_at_beginning(7)
print("aainu hates me")
print_linked_list()

print("she dont like me")

add_at_desired_position(4,"me")

print_linked_list()