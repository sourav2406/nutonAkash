def printTree(root):
    if root:
        print(root.val, end='')
        printTree(root.left)
        printTree(root.right)
