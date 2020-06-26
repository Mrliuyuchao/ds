from typing import List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return 'Node(%s)'%(self.data)

class LinkList:
    def __init__(self):
        self.head = None
    #插入头部节点
    def insert_head(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    # 插入尾部节点
    def append(self,data):
        if self.head is None:
            self.insert_head(data)
        else:
            curr =self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    # 插入中间
    def insert(self,i,data):
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            new_node = Node(data)
            curr = self.head
            pre = curr
            j = 1
            while j<i:
                pre = curr
                curr = curr.next
                j+=1
            pre.next = new_node
            new_node.next = curr

    # 直接构造多元表链表
    def LinkList(self,obj:list):
        new_node = Node(obj[0])
        self.head = new_node
        curr = self.head
        for i in obj[1:]:
            curr.next = Node(i)
            curr = curr.next

    # 删除头部
    def delete_head(self):
        if self.head is None:
            print('空链表')
        else:
            self.head = self.head.next

    #删除尾部
    def pop(self):
        if self.head is None:
            print('空链表')
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None

    #删除尾部2
    def delect_tain(self):
        curr  = self.head
        pre = curr
        if curr is None:
            print('空链表')
        else:
            while curr.next:
                pre = curr
                curr = curr.next
            pre.next =None



    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def __repr__(self):
        curr = self.head
        string_list = ""
        while curr:
            string_list += '%s-->'%(curr)
            curr = curr.next
        return  string_list + 'end'


if __name__ == '__main__':
    ll = LinkList()
    # ll.insert_head(10)
    # ll.insert_head(20)
    # ll.append(23)
    # ll.insert(2,40)
    ll.LinkList([1,2,3,4,5])
    # ll.pop()
    ll.delect_tain()
    ll.print_list()
    print(ll)