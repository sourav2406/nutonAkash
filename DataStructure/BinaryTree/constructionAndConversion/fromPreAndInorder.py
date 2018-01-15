#Construct tree from given Pre Order and In Order tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(arr, start, end, key):
    for i in range(start, end+1):
        if arr[i] == key:
            return i

def buildTree(inOrder, preOrder, inStart, inEnd):
    if inStart > inEnd:
        return None

    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    if inStart == inEnd:
        return tNode

    inIndex = search(inOrder, inStart, inEnd, tNode.data)

    tNode.left = buildTree(inOrder, preOrder, inStart, inIndex-1)
    tNode.right = buildTree(inOrder, preOrder, inIndex+1, inEnd)

    return tNode
def printTree(node):
    if node is None:
        return
    printTree(node.left)
    print(node.data, end=' ')
    printTree(node.right)

#driver function
inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

buildTree.preIndex = 0

root = buildTree(inOrder, preOrder, 0, len(inOrder)-1)

printTree(root)
