# 去重 指定值
from typing import List
# class Solution:
#     def removeDuplicates(self, nums: List[int],val:int) -> int:
#         pre = val
#         show = 0
#         fast = 0
#         while fast < len(nums):
#             if nums[fast] == pre:
#                 fast += 1
#             else:
#                 nums[show] = nums[fast]
#                 fast += 1
#                 show += 1
#         return  show


# 移动零
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        show = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[show] = nums[fast]
                show += 1
                fast += 1
        for i in range(show,len(nums)):
            nums[i] = 0
        return show

if __name__ == '__main__':
    ll = Solution()

    print(ll.removeDuplicates([1,0,2,0,3,4]))


# 和为指定的值

# def towSum(nums:list,target:int):
#         left = 0
#         right = len(nums)-1
#         while left < right:
#             curr = nums[left] + nums[right]
#             if curr == target:
#                 return [left,right]
#             else:
#                 if curr < target:
#                     left += 1
#                 else:
#                     right -= 1
# #
#
# ll = towSum([-5,-4,-3,-2,-1],-8)
# print(ll)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_dict = {}
#         for i in range(len(nums)):
#             temp = target - nums[i]
#             if temp in nums_dict:
#                 return [i,nums_dict[temp]]
#             else:
#                 nums_dict[nums[i]] = i

# class Solution:
#     def twoSum(self,nums:list,target:int):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] +nums[j] == target:
#                     return [i,j]
#         return False
#
# if __name__ == '__main__':
#     num = Solution()
#
#     print(num.twoSum([3,2,4],6))




