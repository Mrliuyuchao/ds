class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print('{}can study hardly'.format(self.name))


stu = Student('lilei', 23)
print(stu.name)
print(stu.age)
stu.study()
