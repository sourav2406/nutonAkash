#Stack implementation 
class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return True if self.root is None else  False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        #print("New node added succesfully!!!")

    def pop(self):
        if self.is_empty():
            return -1
        else:
            poped = self.root.data
            self.root = self.root.next
            return poped

    def peek(self):
        if self.is_empty():
            return -1
        return self.root.data

    def printStack(self):
        if self.is_empty():
            print("Stack is empty!!!")
            return -1
        node = self.root
        while node is not None:
            print(node.data, end=' ')
            node = node.next
        print('\n')

    def is_last(self):
        return True if self.root.next is None else False


#driver programe for this module
if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.printStack()
    stack.push(20)
    stack.printStack()
    stack.push(30)
    stack.printStack()
    stack.pop()
    stack.printStack()
    stack.pop()
    stack.printStack()
    stack.pop()
    stack.printStack()
    stack.pop()

