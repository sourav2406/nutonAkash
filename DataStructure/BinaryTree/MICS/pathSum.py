class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pathSum(node, s):
    if node is None:
        return (s == 0)
    else:
        #ans = False
        subSum = s - node.data

        if subSum == 0 and node.left is None and node.right is None:
            return True

        if node.left is not None:
            return False or pathSum(node.left, subSum)
        if node.right is not None:
            return False or pathSum(node.right, subSum)

        #return ans

# Driver program to test above functions
 
s = 21
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.right = Node(5)
root.left.left = Node(3)
root.right.left = Node(2)
 
if pathSum(root, s):
    print("There is a root-to-leaf path with sum {}".format(s))
else:
    print("There is no root-to-leaf path with sum {}".format(s))