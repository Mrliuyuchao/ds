class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return "Node(%s)"%(self.data)

class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self,index):
        curr = self.head
        for _ in range(1,index):
            curr =curr.next
        return curr

    def insert(self,index,data):
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise Exception('索引越界')
        elif self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            pre = self.get(index-1)
            new_node.next = pre.next
            pre.next = new_node
        self.size += 1


    def remove(self,index):
        if index < 0 or index >= self.size:
            raise Exception('索引越界')
        elif index == 0:
            remove_node = self.head
            self.head= self.head.next
        elif index == self.size:
            pre = self.get(index-1)
            remove_node = pre.next
            pre.next =None
            self.tail = pre
        else:
            pre = self.get(index)
            remove_node = pre.next
            pre.next = pre.next.next

        self.size -= 1
        return  remove_node.data

    def reverse(self):
        pre = None
        curr = self.head
        while curr:
            temp = curr.next
            if pre is None:
                curr.next = pre
            else:
                curr.next = pre
            pre = curr
            curr = temp
        self.head = pre

    def __repr__(self):
        curr = self.head
        string =''
        while curr:
            string += '%s-->'%(curr)
            curr =curr.next
        return string +'end'

if __name__ == '__main__':
    l = LinkList()
    l.insert(0,1)
    l.insert(1,2)
    l.insert(2,3)
    l.insert(1,20)
    # print(l.remove(3))
    # l.remove(2)

    print(l)
    l.reverse()
    print(l)
