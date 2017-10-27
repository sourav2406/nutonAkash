import treeNode

def printLevelOrder(node):
    print('\n')
    if node is None:
        return

    queue = []

    queue.append(node)
    while queue:
        print(queue[0].val, end='')
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


ROOT = treeNode.Node(1)
ROOT.left = treeNode.Node(2)
ROOT.right = treeNode.Node(3)
ROOT.left.left = treeNode.Node(4)
ROOT.left.right = treeNode.Node(5)
ROOT.right.left = treeNode.Node(6)
ROOT.right.right = treeNode.Node(7)

treeNode.printTree(ROOT)

printLevelOrder(ROOT)
