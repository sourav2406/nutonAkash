#Implementing queue using stack
from stack import Stack

class Queue:
    def __init__(self):
        self.queueStack = Stack()

    def push(self,data):
        self.queueStack.push(data)

    def popInner(self):
        if self.queueStack.is_last():
            return self.queueStack.pop()

        temp = self.queueStack.pop()
        result = self.popInner()
        self.queueStack.push(temp)
        return result

    def pop(self):
        if self.queueStack.is_empty() is not True:
            self.popInner()


    def printQueue(self):
        self.queueStack.printStack()


if __name__ == '__main__':
    queue = Queue()
    queue.push(10)
    queue.push(20)
    queue.push(30)
    queue.push(40)
    queue.printQueue()
    queue.pop()
    queue.printQueue()
    queue.pop()
    queue.printQueue()
    queue.pop()
    queue.printQueue()
    queue.pop()
    queue.printQueue()
    queue.pop()
