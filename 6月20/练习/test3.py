from typing import List
class LinkList:
    def LinkList(self,val,obj:list):
        list1 = len(obj)
        fl = 0
        for i in range(list1):
            if obj[i] != val:
                obj[fl],obj[i] = obj[i],obj[fl]
                fl += 1

        print()
        print(fl,obj[:fl])

if __name__ == '__main__':
    ll = LinkList()
    ll.LinkList(2,[0,1,2,2,3,0,4,2])
