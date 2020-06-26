# from typing import List
# class Solution:
#     def removeDiplicatrd(self,nums:List [ int ]) -> int:
#         n = len(set(nums))
#         i = 0
#         while i < n-1:
#             if nums[i] == nums[i+1]:
#                 temp = nums[i+1]
#                 nums[i+1:len(nums)-1] = nums[i+2:]
#                 nums[-1] = temp
#                 continue
#             else:
#                 i += 1
#         return i+1
# if __name__ == '__main__':
#     ll = Solution()
#     ll.removeDiplicatrd([1,1,2,2,3,4])
#     print(ll.removeDiplicatrd([1,1,2,2,3,4]))



from typing import List
class Solution:
    def removeDiplicatrd(self,nums:List [ int ]) -> int:
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[fast] == nums[slow] :
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1

if __name__ == '__main__':
    ll = Solution()
    print(ll.removeDiplicatrd([1,1,2,2,3,4]))