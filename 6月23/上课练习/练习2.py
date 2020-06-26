from typing import Any,Optional,NoReturn
class Node:
    def __init__(self,data:Any,next:Optional = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return 'Node(%s)'%(self.data)


class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self,item):
        node = Node(item)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        node = self.top
        if self.top is None:
            raise  IndexError ('pop from empty stack')
        else:
            self.top = node.next
            return node.data

    def is_empty(self):
        return self.top is None

    def __repr__(self):
        curr = self.top
        string = ''
        while curr:
            string += '%s-->'%(curr)
            curr = curr.next
        return string +'end'

if __name__ == '__main__':
    stack = LinkedStack()
    stack.push(2)
    stack.push(9)
    stack.push('python')
    print(stack)
    stack.pop()
    print(stack)
    print(stack.is_empty())


