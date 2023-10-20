class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def add_node(root,data):
    if root == None:
        newnode = Node(data)
        root = newnode
        return root
    

def create_bt(root,arr,i):

    if i < len(arr):
        root = add_node(root,arr[i])
        root.left = create_bt(root.left,arr,i= 2 * i + 1)
        root.right = create_bt(root.right,arr,i= 2 * i + 2)

    return root

def create_bst(root,data):
    if root == None:
        root = add_node(root,data)
        return root
    elif data < root.data:
        root.left = create_bst(root.left,data)
    
    else:
        root.right = create_bst(root.right,data)
    
    root.height = max(get_height(root.left),get_height(root.right)) + 1
    bf = get_bf(root)

    if bf > 1:
        # Letf-left subtree cases
        # LL
        if data < root.left.data:
            return RR_rotation(root)
        # LR
        else:
            root.left = LL_rotate(root.left)
            return RR_rotation(root)
    
    if bf < -1:
        # RR
        if data > root.right.data:
            return LL_rotate(root)
        # RL
        else:
            root.right = RR_rotation(root.right)
            return LL_rotate(root)

    return root
# main rotation logic...

# LL
# RR
def LL_rotate(root):
    if root == None or root.left == None and root.right == None:
        return root
    print("LL ROTATE")
    y = root.right
    t2 = y.left
    y.left = root
    root.right = t2
    root.height = max(get_height(root.left),get_height(root.right)) + 1
    y.height = max(get_height(y.left),get_height(y.right)) + 1
    return y


def RR_rotation(root):
    print("RR rotate")
    y = root.left
    t2 = y.right
    root.left = t2
    y.right = root
    root.height = max(get_height(root.left),get_height(root.right)) + 1
    y.height = max(get_height(y.left),get_height(y.right)) + 1
    return y

left_size = 0
right_size = 0

def get_height(root):
    if root == None:
        return 0
    
    return root.height

def get_bf(root):
    if root == None:
        return 0
    return get_height(root.left) - get_height(root.right)

def update_height(root):
    if root != None:
        root.height = max(get_height(root.left),get_height(root.right)) + 1
        return
    

def print_node(root):
    if root == None:
        return
    
    print_node(root.left)
    print(root.data)
    print_node(root.right)

def get_size(root):
    if root == None:
        return 0
    
    return get_size(root.left) + get_size(root.right) + 1

def delete_node(root,data,prev):
    if root == None:
        return root
    
    if data == root.data and root.left == None and root.right == None:
        if prev.left == root:
            prev.left = None
            root = prev.left
            return root
        else:
            prev.right = None
            root = prev.right
            return root
    if data < root.data:
        root.left = delete_node(root.left,data,root)
        root.height = get_height(root)
    elif data == root.data:
        print('data found')
        if root.left:
            if root.left.right != None:
                temp = root.left.right.data
                root.left.right.data = root.data
                root.data = temp
                delete_node(root.left.right,data,root.left)
            else:
                temp = root.left.data
                root.left.data = root.data
                root.data = temp
                delete_node(root.left,data,root)

        elif root.right:
            if root.right.left != None:
                temp = root.data
                root.data = root.right.left
                root.right.left = temp
                delete_node(root.right.left,data,root.right)

            else:
                temp = root.data
                root.data = root.right.data
                root.right.data = temp
                delete_node(root.right,data,root)
    else:
        root.right = delete_node(root.right,data,root)

    bf = get_bf(root)

    if bf > 1:
        if get_bf(root.left) >= 0:
            root = RR_rotation(root)
            return  root
        else:
            root.left = LL_rotate(root.right)
            root = RR_rotation(root)
            return root
        
    elif bf < 0:
        if get_bf(root.right) > 0:
            root.right = RR_rotation(root.right)
            root = LL_rotate(root)
            return root
        else:
            root = LL_rotate(root)
            return root
        
    return root

arr = [10,13,11,14,12,15]
root = None
for i in arr:
    root = create_bst(root,i)

# root = delete_node(root,8,None)
# root = delete_node(root,13,None)
# root = delete_node(root,61,None)
# root = delete_node(root,6,None)
update_height(root)
print(get_height(root))
print("root = ", root.data)
print('after deleting node 12')
root = delete_node(root,12,None)
print_node(root)

