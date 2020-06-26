# 双指针去重指定的值
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int],val:int) -> int:
        pre = val
        show = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == pre:
                fast += 1
            else:

                nums[show] = nums[fast]
                fast += 1
                show += 1
        return  show

if __name__ == '__main__':
    ll = Solution()
    print(ll.removeDuplicates([1,1,2,2,3,4],2))


# from typing import List
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         show = 0
#         fast = 0
#         while fast < len(nums):
#             if nums[fast] == 0:
#                 fast += 1
#             else:
#                 nums[show],nums[fast] = nums[fast],nums[show]
#                 show += 1
#                 fast += 1
#         return show,nums
# if __name__ == '__main__':
#     ll = Solution()
#     print(ll.removeDuplicates([0,1,0,3,12]))


# from typing import List
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         show = 0
#         fast = 1
#         count = 1
#         while fast < len(nums):
#             if nums[fast] == nums[show]:
#                 if count>=2:
#                     fast += 1
#                 else:
#                     count += 1
#                     show += 1
#                     nums[show] =nums[fast]
#                     fast += 1
#             else:
#                 count = 1
#                 show += 1
#                 nums[show] = nums[fast]
#                 fast += 1
#         return nums
# if __name__ == '__main__':
#     ll = Solution()
#     print(ll.removeDuplicates([1,1,2,2,3,3]))


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# def is_creat(head):
#     curr = head
#     pre = head
#     while curr and curr.next:
#         pre = pre.next
#         curr = curr.next.next
#         if pre == curr:
#             return  True
#     return False
#
# if __name__ == '__main__':
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)
#     node5 = Node(5)
#     node6 = Node(6)
#     node7 = Node(7)
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node5
#     node5.next = node6
#     node6.next = node7
#     node7.next = node4
#     print(is_creat(node1))