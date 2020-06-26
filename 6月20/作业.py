class Array:
    def __init__(self,capacity):
        self.array = [None] * capacity
        self.size = 0
    def insert(self,index,element):
        if index < 0 or index > self.size:
            print('数组越界')
        if self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size - 1 , index -1 ,-1):
            self.array[i+1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def remove(self,index):
        if index < 0 or index > self.size:
            print("数组越界")
        for i in range(index,self.size):
            self.array[i] = self.array[i+1]
        self.size -= 1

    def addcapacity(self):
       new_array = [None] * len(self.array) * 2
       for i in range(self.size):
           new_array[i] = self.array[i]
       self.array = new_array

    def output(self):
        for i in range(self.size):
            print(self.array[i],end='-->')

    def result(self):
        new_array = self.array
        if self.array[0] == 0:
            print('第一位数为0,0不能做除数')
        for i in range(self.size):
            new_array = self.array[i]/self.array[0]
            print(new_array,end='-->')

if __name__ == '__main__':
    work = Array(4)
    work.insert(0,1)
    work.insert(1,2)
    work.insert(2,3)
    work.insert(3,4)
    work.insert(4,5)
    work.result()
    # work.output()

