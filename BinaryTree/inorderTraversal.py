from treeNode import Node

def inorder(root):
    if root:
        inorder(root.left)

        print(root.val)

        inorder(root.right)

if __name__ == '__main__':
    ROOT = Node(1)
    ROOT.left = Node(2)
    ROOT.right = Node(3)

    inorder(ROOT)

    #print(ROOT.val)
    #print(ROOT.left.val)
    #print(ROOT.right.val)
    