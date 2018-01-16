#Construct Special binary tree from given two special preorder arr
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def consructTree(preOrder, spslArr, n):
    global index
    if index == n:
        return None

    temp = Node(preOrder[index])
    index += 1
    
    if spslArr[index-1] == 'N':
        temp.left = consructTree(preOrder, spslArr, n)
        temp.right = consructTree(preOrder, spslArr, n)

    return temp

def printTree(node):
    if node is None:
        return
    printTree(node.left)
    print(node.data, end=' ')
    printTree(node.right)

#Driver Programe
preA = [10, 30, 20, 5, 15]
spsl = ['N', 'N', 'L', 'L', 'L']

index = 0
root = consructTree(preA, spsl, len(preA))
printTree(root)