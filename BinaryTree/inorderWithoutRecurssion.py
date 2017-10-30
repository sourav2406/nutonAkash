import treeNode

def inorder(root):
    current = root
    s = []
    done = 0
    print('\n')
    while not done:
        #print("here:")
        if current is not None:
            s.append(current)
            current = current.left
        else:
            if s:
                current = s.pop()
                print(current.val, end='')
                current = current.right
            else:
                done = 1


if __name__ == '__main__':
    ROOT = treeNode.Node(1)
    ROOT.left = treeNode.Node(2)
    ROOT.right = treeNode.Node(3)
    ROOT.left.left = treeNode.Node(4)
    ROOT.left.right = treeNode.Node(5)
    ROOT.right.left = treeNode.Node(6)
    ROOT.right.right = treeNode.Node(7)

    treeNode.printTree(ROOT)

    inorder(ROOT)
