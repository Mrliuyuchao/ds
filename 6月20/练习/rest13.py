from typing import List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node(%s)'%(self.data)


class LinklistL:
    def __init__(self):
        self.head = None

    def insert_head(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def append(self,data):
        curr = self.head
        if self.head is None:
            self.insert_head(data)
        else:
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def insert(self,i,data):
        new_node = Node(data)
        curr = self.head
        pre = curr
        if self.head is None or i==1:
            self.insert_head(data)
        else:
            j = 1
            while j<i:
                pre = curr
                curr = curr.next
                j+=1
            pre.next = new_node
            new_node.next = curr


    def LinkList(self,obj:list):
        new_node = Node(obj[0])
        self.head = new_node
        curr = self.head
        for i in obj[1:]:
            curr.next = Node(i)
            curr = curr.next

    def delect_head(self):
        if self.head is None:
            print('空链表')
        else:
            self.head = self.head.next

    def pop(self):
        curr = self.head
        if self.head is None:
            print('空链表')
        else:
            while curr.next.next:
                curr = curr.next
            curr.next = None


    def deldect_tail(self):
        curr = self.head
        pre = self.head
        if self.head is None:
            print('空链表')
        else:
            while curr.next:
                pre = curr
                curr = curr.next
            pre.next = None


    def print_list(self):
        temp =self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def __repr__(self):
        curr =self.head
        stying_lisr = ""
        while curr:
            stying_lisr += '%s-->'%(curr)
            curr = curr.next
        return stying_lisr +'end'


if __name__ == '__main__':
    ll = LinklistL()
    ll.insert_head(2)
    ll.append(4)
    ll.insert(1,3)
    ll.LinkList([1,2,3,4,5])
    ll.delect_head()
    ll.pop()
    ll.deldect_tail()
    ll.print_list()
    print(ll)