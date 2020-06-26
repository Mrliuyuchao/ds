"""
leetcode第026题数组去重(删除排序数组中的重复项)

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
"""


# 方法一
from typing import List
# class Solution:
#     def removeDuolicated(self,nums:list):
#         show = 0
#         fast = 1
#         while fast <len(nums):
#             if nums[fast] == nums[show]:
#                 fast += 1
#             else:
#                 show += 1
#                 nums[show] = nums[fast]
#                 fast += 1
#         return show + 1,nums


# 方法二
class Solution:
    def removeDuolicated(self,nums:List):
        n = len(set(nums))
        i = 0
        while i < n -1:
            if nums[i] == nums[i+1]:
                temp = nums[i+1]
                nums[i+1:len(nums) -1 ] = nums[i+2:]
                nums[-1] = temp
                continue
            else:
                i+=1
        return i + 1,nums


if __name__ == '__main__':
    test = Solution()
    print(test.removeDuolicated([1,1,2,4,4,5]))
