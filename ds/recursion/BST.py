class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def add_Node(root,data):
    if root == None:
        newnode = Node(data)
        root = newnode
        return root
    if data < root.data:
        root.left = add_Node(root.left,data)
        return root
    elif data > root.data:
        root.right = add_Node(root.right,data)
        return root

def display_nodes(root):
    if root == None:
        return
    display_nodes(root.left)
    print(root.data)
    display_nodes(root.right)

def print_all_leaf_node(root):
    if root == None:
        return
    
    if root.left == None and root.right == None:
        print(root.data)
        return
    
    if root.left != None:
        print_all_leaf_node(root.left)

    if root.right != None:
        print_all_leaf_node(root.right)

root = None
root = add_Node(root,100)
add_Node(root,80)
add_Node(root,90)
add_Node(root,120)
add_Node(root,50)
add_Node(root,110)
add_Node(root,140)
add_Node(root,30)
add_Node(root,60)
add_Node(root,85)
add_Node(root,95)
add_Node(root,115)
add_Node(root,150)
# display_nodes(root)
print(print_all_leaf_node(root))
print("Hello World")