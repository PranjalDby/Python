class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def add_node(root,data):
    if root == None:
        newnode = Node(data)
        root = newnode
        return root
    
def insert_left(root,data):
    if root == None:
        root = add_node(root,data)
        return root
    
    root.left = insert_left(root.left,data)
    return root

def insert_right(root,data):
    if root == None:
        root = add_node(root,data)
        return root
    
    root.right = insert_left(root.right,data)
    return root

def create_bt(root,arr,i):
    if i < len(arr):
        root = add_node(root,arr[i])
        root.left = create_bt(root.left,arr,i= 2 * i + 1)
        root.right = create_bt(root.right,arr,i= 2 * i + 2)

    return root

def create_bt_itr(arr,i):
    st = []
    root = None
    root = add_node(root,arr[i])
    st.append(root)
    i+=1
    while len(st) != 0:
        curr = st.pop()
        if i < len(arr):
            curr.left = add_node(curr.left,arr[i])
            st.append(curr.left)
            i+=1

        if i < len(arr):
            curr.right = add_node(curr.right,arr[i])
            st.append(curr.right)
            i+=1

    return root

def insert_after(root,data,after):
    if root ==  None:
        return
    if after == root.data:
        newnode = Node(data)
        if root.right == None:
            root.right = newnode
            return
        
        if root.right.left == None:
            root.right.left = newnode
            return
    insert_after(root.left,data,after)
    insert_after(root.right,data,after)

def insert_before(root,data,before):
    if root == None:
        return
    
    if before == root.data:
        newnode = Node(data)
        if root.left == None:
            root.left = newnode
            return
        
        if root.left.left == None:
            root.left.left = newnode
            return
    insert_before(root.left,data,before)
    insert_before(root.right,data,before)

def delete_pred(root,node):
    if root == None:
        return
    
    else:
        if node.left == None and node.right == None:
            node.data = None
            return
        else:

            if node.left:
                if node.left.right != None:
                    temp = node.data
                    node.data =  node.left.right.data
                    node.left.right.data = temp
                    return delete_pred(root,node.left.right)
                else:
                    temp = node.data
                    node.data = node.left.data
                    node.left.data = temp
                    return delete_pred(root,node.left)
                
            if node.right:
                if node.right.left != None:
                    temp = node.data
                    node.data = node.right.left
                    node.right.left = temp
                    return delete_pred(root,node.right.left)
                
                else:
                    temp = node.data
                    node.data = node.right.data
                    node.right.data = temp
                    return delete_pred(root,node.right)
            
def print_node(root):
    if root == None:
        return
    
    print_node(root.left)
    print(root.data)
    print_node(root.right)

arr = ['A','B','C','D','E','F']
# insert 32 after 14
root = None
root = create_bt(root,arr,0)
# insert_after(root,'H','A')
print("Insert before")
# insert_after(root,'S','B')
insert_before(root,'G','E')
delete_pred(root,root.left.left)
delete_pred(root,root.left)
print_node(root)