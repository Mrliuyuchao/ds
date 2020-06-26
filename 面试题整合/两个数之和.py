from typing import List
# 第一种方法
# def twoSum(nums:list,target:int):
#     left = 0
#     right = len(nums) -1
#     while left < right:
#         curr = nums[left] + nums[right]
#         if curr == target:
#             return [left,right]
#         else:
#             if curr < target:
#                 left += 1
#             else:
#                 right -= 1
#
# ll = twoSum([-5,-4,-3,-2,-1],-8)
# print(ll)


# 第二种方法
# class Solution:
#     def twoSum(self,nums:list,target:int):
#         new_sums = {}
#         for i in range(len(nums)):
#             temp = target - nums[i]
#             if temp in new_sums:
#                 return [new_sums[temp],i]
#             else:
#                 new_sums[nums[i]] = i

# 第三种方法
class Solution:
    def twoSum(self,nums:list,target:int):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

if __name__ == '__main__':
    num = Solution()

    print(num.twoSum([3,2,4],6))