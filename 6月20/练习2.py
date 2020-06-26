
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node(%s)'%(self.data)

class LinkList:
    def __init__(self):
        self.head = None

    #头部插入节点
    def insert_head(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


    def __repr__(self):
        current = self.head
        string_repr = ''
        while current:
            string_repr += '%s -->'%(current)
            current = current.next
        return string_repr + "end"
if __name__ == '__main__':
    ll = LinkList()
    ll.insert_head(100)
    ll.insert_head(99)
    ll.insert_head(98)
    ll.print_list()
    print('-----------------------------------------------')
    print(ll)