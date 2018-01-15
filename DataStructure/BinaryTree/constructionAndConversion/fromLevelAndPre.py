#construct tree with given inorder and level order arrays
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTree(node):
    if node is None:
        return
    printTree(node.left)
    print(node.data, end=' ')
    printTree(node.right)

def search(arr, start, end, key):
    for i in range(start, end+1):
        if arr[i] == key:
            return i
    return -1

def getNewLevelOrder(inOrder, levelOrder, inStart, inEnd):
    newLevel = []
    for key in levelOrder:
        if search(inOrder,inStart, inEnd, key) != -1:
            newLevel.append(key)
    return newLevel

def buildTree(inOrder, levelOrder, inStart, inEnd):
    if inStart > inEnd:
        return None

    tNode = Node(levelOrder[0])

    if inStart == inEnd:
        return tNode

    inIndex = search(inOrder, inStart, inEnd, tNode.data)

    llevelOrder = getNewLevelOrder(inOrder, levelOrder, inStart, inIndex-1)
    rlevelOrder = getNewLevelOrder(inOrder, levelOrder, inIndex+1, inEnd)
    
    tNode.left = buildTree(inOrder, llevelOrder, inStart, inIndex-1)
    tNode.right = buildTree(inOrder, rlevelOrder, inIndex+1, inEnd)
    
    del llevelOrder[:]
    del rlevelOrder[:]

    return tNode

#driver programe
inOrder = [4, 8, 10, 12, 14, 20, 22]
levelOrder = [20, 8, 22, 4, 12, 10, 14]

node = buildTree(inOrder, levelOrder, 0, len(inOrder)-1)
printTree(node)

