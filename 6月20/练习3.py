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
    # 头部插入节点
    def insert_head(self,data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
        self.head=new_node

    # 尾部插入节点
    def append(self,data):
        if self.head is None:
            self.insert_head(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    # 中间插入节点
    def insert(self, i , data):
        if self.head is None or i ==1:
            self.head = self.insert_head(data)
        else:
            new_node = Node(data)
            curr = self.head
            pre = curr
            j=1
            while j<i:
                pre = curr
                curr = curr.next
                j+=1
            pre.next = new_node
            new_node.next = curr

    # 直接构建多元表链表
    def LinkList(self,obj:List):
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

    # 删除尾部
    def pop(self):
        curr = self.head
        if self.head is None:
            print('空链表')
        else:
            while curr.next.next:
                curr = curr.next
            temp = curr.next
            curr.next = None
        return temp

    # 删除尾部
    def delect_tail(self):
        curr = self.head
        pre = self.head
        if self.head is None:
            print('空链表')
        else:
            while curr.next:
                pre = curr
                curr = curr.next
            temp = pre.next
            pre.next = None
        return temp

    def print_list(self):
        cuttent = self.head
        while cuttent:
            print(cuttent.data)
            cuttent = cuttent.next

    def __repr__(self):
        temp = self.head
        string_list = ""
        while temp:
            string_list += '%s -->'%(temp)
            temp = temp.next
        return string_list + 'end'

if __name__ == '__main__':
    ll = LinkList()
    # ll.insert_head(1)
    # ll.append(2)
    # ll.insert(2,20)
    ll.LinkList([1,2,3,4,5])
    print(ll)
    ll.delete_head()
    # ll.delect_tail()
    # print(ll.delect_tail())
    ll.pop()
    print(ll.pop())
    ll.print_list()
    print(ll)
