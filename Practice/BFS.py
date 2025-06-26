from collections import deque

# __init__ creates and sets up the object
# root = Treenode(1) stores a reference to the object that was just created
# Think of __init__ as baking a cake.
# And root = Treenode(1) as putting a label on the cake saying “🎂 Birthday Cake”.
#root is a reference (a variable) pointing to the entire node object in memory.
#This node object has fields:
#.val → the actual value stored (like 1)
#.left → reference to the left child (or None)
#.right → reference to the right child (or None)

class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return []
    
    res = []
    q = deque([root])

    while q:
        level_size = len(q)
        level_nodes = []

        for _ in range(level_size):
            node = q.popleft()    #Get the root node to append it
            level_nodes.append(node.val)

            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
                
        res.append(level_nodes)
    return res

root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)

print(bfs(root))


