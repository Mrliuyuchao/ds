class Array:
    def __init__(self,cape):
        self.arrty = [None] * cape
        self.size = 0

    def  insert(self,index,element):
        if index < 0 or index > self.size:
            raise Exception('数组越界')
        if self.size >= len(self.arrty):
            arrty.addkuorong()
        for i in range(self.size-1,index-1,-1):
            self.arrty[i+1] = self.arrty[i]
        self.arrty[index] = element
        self.size += 1

    def output(self):
        for i in range(self.size):
            print(self.arrty[i],end='->')

    def addkuorong(self):
        new_arrty = [None] * len(self.arrty) * 2
        for i in range(self.size):
            new_arrty[i] = self.arrty[i]
        self.arrty = new_arrty

if __name__ == '__main__':
    arrty = Array(4)
    arrty.insert(0,0)
    arrty.insert(1,1)
    arrty.insert(2,2)
    arrty.insert(3,3)
    arrty.insert(4,4)
    arrty.output()