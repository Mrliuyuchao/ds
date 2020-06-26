class Node: #节点类
    def __init__(self,data):
        self.data = data
        self.next = 0

    def __repr__(self):
        # return 'Node(%s)'%self.data
        # return f"Node({self.data})"
         return 'Node({})'.format(self.data)

if __name__ == '__main__':
    n = Node(0)
    print(n)