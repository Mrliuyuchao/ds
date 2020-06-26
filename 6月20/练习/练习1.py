from typing import List

class Node:
    def __init__(self,capacity):
        self.data =[None] * capacity
        self.next = None
    def __repr__(self):
        return self.data

class LinkList:
    def __init__(self):
        self.head = None

    def insert_head(self,data):
        new_data = Node(data)
        if self.head:
            new_data.next = self.head
        self.head = new_data

    def append(self,data):
        if self.head is None:
            self.insert_head(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            self.head = curr

    def LinkLost(self,obj:list):
        list1 =[]
        list1.append(obj[0])
        for i in obj:
            if i != list1[len(list1)-1]:
                list1.append(i)
        print(obj)
        print(list1,len(list1))

if __name__ == '__main__':
    ll = LinkList()
    ll.LinkLost([1,1,2,2,3,4,4,5])
