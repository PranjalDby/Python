# properties to know about binary trees
"""
@ a tree is a binary tree if its parent node has atmost two children's.

@there is exactly 1 root node (that has no parents).

@ there should be exactly one path b/w root and any other node

@ to get the left node = 2 * i + 1 i = level 0  and right node = 2 * i + 2 an get the parent = i / 2
"""
import numpy as np
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

def print_node(root):
    if root == None:
        return
    
    print_node(root.left)
    print(root.data)
    print_node(root.right)

def dfs(root):
    if root == None:
        return
    
    stack = [root]

    while len(stack) > 0:
        curr = stack.pop()
        print(curr.data)
        if curr.right != None:
            print("right cvalue")
            stack.append(curr.right)

        print(".......")

        if curr.left != None:
            stack.append(curr.left)

lists = []
def recursive_dfs(root):
    if root == None:
        return None
    
    left_values = recursive_dfs(root.left)
    right_values = recursive_dfs(root.right)
    return [root.data , left_values , right_values]


queue = []
def bfs(root):
    lists = []
    if root == None:
        return []
    
    if len(queue) == 0:
        queue.append(root)
    while len(queue) > 0:
        curr = queue.pop(0)
        lists.append(curr.data)
        if curr.left != None:
            queue.append(curr.left)
        
        if curr.right != None:
            queue.append(curr.right)

    return lists


root = None
root = add_Node(root,12)
add_Node(root,23)
add_Node(root,32)
add_Node(root,10)
add_Node(root,6)
add_Node(root,30)
add_Node(root,40)
add_Node(root,50)

print(bfs(root))

