#Construct binary tree from linked list
class linkedList:
    def __init__(self,data):
        self.data = data
        self.next = None


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Conversion:
    def __init__(self,data=None):
        self.head = None
        self.root = None

    def push(self, data):
        new_node = linkedList(data)
        new_node.next = self.head
        self.head = new_node

    def inOrderPrint(self, node):
        if node is None:
            return
        self.inOrderPrint(node.left)
        print(node.data, end=' ')
        self.inOrderPrint(node.right)

    def convertList2Binary(self):
        q = []
        if self.head is None:
            self.root = None
            return

        self.root = Node(self.head.data)
        q.append(self.root)
        self.head = self.head.next

        while self.head is not None:
            parent = q.pop(0)
            leftChild = None
            rightChild = None

            leftChild = Node(self.head.data)
            q.append(leftChild)

            self.head = self.head.next
            if self.head is not None:
                rightChild = Node(self.head.data)
                q.append(rightChild)
                self.head = self.head.next

            parent.left = leftChild
            parent.right = rightChild

# Driver Program to test above function
 
# Object of conversion class
conv = Conversion()
conv.push(36)
conv.push(30)
conv.push(25)
conv.push(15)
conv.push(12)
conv.push(10)
 
conv.convertList2Binary()
 
print("Inorder Traversal of the contructed Binary Tree is:")
conv.inOrderPrint(conv.root)
print('\n')

