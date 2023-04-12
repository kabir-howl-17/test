'''Q-2 ) Write postorder and inorder traversal function for the tree given
below, including declaring classes, providing input, and perform the dry
run also. (5 marks)'''


class Node:

    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None


root = Node(3)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(5)
root.left.right = Node(4)
root.right.right = Node(7)

def preorder(root):    # in preorder we go travel through root then left and then right
    if root == None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

preorder(root)
print("------------------")

def inorder(root):    #in inorder we travel through left then root and then right
    if root == None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

inorder(root)