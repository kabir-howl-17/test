#1. Write a Python program to find the size of a singly linked list.

#2. Write a Python program to search a specific item in a singly linked list and return true 
# if the item is found otherwise return false

#
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


# will tell the size of the linklist
def size():
    global head 
    c = 1
    cur = head 
    if head == None:
        return -1 
    while (cur.next != None):
        c = c + 1
        cur = cur.next
    return c        


# will search the element of that
def search(target):
    global head 
    cur = head 

    while (cur.next != None):
        cur = cur.next
        if target == cur.data :
            return True
    return False

    #sol 2
    #while(target!= cur.data):
    #    cur = cur.next
    #   return True    
    #return False


# to get element in that ll
def access(k):
    global head 
    cur = head 
    c = 0

    i = size()
    if i-1 < k:
        return "not in list"
    while (c!=k):
        cur = cur.next
        c = c + 1   
    return cur.data 
def alter(k, alt):
    global head
    cur = head
    c = 0

    i = size()
    if i-1 < k:
        return "not here buddy"
    while c != k :
        cur = cur.next
        c = c + 1
    cur.data = alt
    return cur.data


    






#driver code

add_node_at_end(17)
add_node_at_end(62)
add_node_at_end(28)
add_node_at_end(23)
add_at_beginning(7)
add_at_desired_position(4,"me")

print("------------------")
print_linked_list()

print("---------------")
g = access(5)
print(g)

f = alter(3,"her")
print_linked_list()