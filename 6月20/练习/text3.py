class Array:
    def __init__(self,capacity):
        self.array =[None] * capacity
        self.size = 0

    def inset(self,index,element):
        if index < 0 or index > self.size:
            raise  Exception ('数组越界')
        if self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size - 1 ,index - 1 , -1):
            self.array[i+1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def remove(self,index):
        if index < 0 or index > self.size:
            raise Exception('数组越界')
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -=1

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def output(self):
        for i in range(self.size):
            print(self.array[i],end='->')

if __name__ == '__main__':
    ll = Array(4)
    ll.inset(0,1)
    ll.inset(1,2)
    ll.inset(2,3)
    ll.inset(3,4)
    ll.inset(4,5)
    # ll.output()
    ll.remove(2)
    ll.output()