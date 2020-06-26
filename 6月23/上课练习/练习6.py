from typing import List
# class Solution:
#     def removeDuplicates(self,nums:List,val:int):
#         show = 0
#         fast = 0
#         while fast < len(nums):
#             if nums[fast] == val:
#                 fast += 1
#             else:
#                 nums[show] = nums[fast]
#                 show += 1
#                 fast += 1
#
# if __name__ == '__main__':
#     ll = Solution()
#     ll.removeDuplicates([1,1,2,3,2,4],2)
#     print(ll.removeDuplicates([1,1,2,3,2,4],2))

#
# class Solution:
#     def removeDuplicates(self,nums:list):
#         show = 0
#         fast = 0
#         while fast < len(nums):
#             if nums[fast] == 0:
#                 fast +=1
#             else:
#                 nums[show] = nums[fast]
#                 show += 1
#                 fast += 1
#         for i in range(show,len(nums)):
#             nums[i] = 0
#         return show,nums
#
# if __name__ == '__main__':
#     ll = Solution()
#     ll.removeDuplicates([1,1,2,0,2,4])
#     print(ll.removeDuplicates([1,So0,2,0,3,4]))


# class Solution:
#     def removeDuplicates(self,nums:list,target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return [i,j]
#         return False


# class Solution:
#     def removeDuplicates(self,nums:list,targer):
#         nums_dict = {}
#         for i in range(len(nums)):
#             temp = targer - nums[i]
#             if temp in nums_dict:
#                 return [nums_dict[temp]+1,i+1]
#             else:
#                 nums_dict[nums[i]] = i

class Solution:
    def removeDuplicates(self,nums:list,targer):
        left = 0
        right = len(nums) - 1
        count  = 0
        for i in range(0,len(nums)):
            if nums[i] <0:
                count += 1
            else:
                break
        if nums[0] < 0 and count == len(nums):
            for i in range(0, len(nums) // 2):
                nums[right - i], nums[i] = nums[i], nums[right - i]
            print(nums)
        while left < len(nums) :
            curr = nums[left] + nums[right]
            if curr == targer:
                    if nums[0] < 0 and count == len(nums):
                        left1 = len(nums) -1- left
                        right1 = len(nums) -1 -right
                        return [right1, left1]
                    else:
                        if left < right:
                            return [left, right]
                        else:
                            return [right, left]
            else:
                if curr < targer :
                    left += 1
                elif right == left + 1:
                    right = len(nums)-1
                else:
                    right -= 1


if __name__ == '__main__':
    ll = Solution()
    print(ll.removeDuplicates([3,2,4],6))