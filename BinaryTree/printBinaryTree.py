def printTree(root):
    if root:
        print(root.val)
        printTree(root.left)
        printTree(root.right)