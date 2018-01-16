#Disance between two nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pathToNode(root, path, k):
    if root is None:
        return False

    path.append(root.data)

    if root.data is k:
        return path

    if (root.left != None and pathToNode(root.left, path, k)) or (root.right != None and pathToNode(root.right, path, k)):
        return True

    path.pop()
    return False

def distance(root, data1, data2):
    if root:
        path1 = []
        pathToNode(root, path1, data1)

        path2 = []
        pathToNode(root, path2, data2)

        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1

        return (len(path1)+len(path2)-2*i)
    else:
        return 0

# Driver Code to test above functions
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right= Node(7)
root.right.left = Node(6)
root.left.right = Node(5)
root.right.left.right = Node(8)
 
dist = distance(root, 4, 5)
print("Distance between node {} & {}: {}".format(4, 5, dist))
 
dist = distance(root, 4, 6)
print("Distance between node {} & {}: {}".format(4, 6, dist)) 
 
dist = distance(root, 3, 4)
print("Distance between node {} & {}: {}".format(3, 4, dist))
 
dist = distance(root, 2, 4)
print("Distance between node {} & {}: {}".format(2, 4, dist))
 
dist = distance(root, 8, 5)
print("Distance between node {} & {}: {}".format(8, 5, dist))