from  typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num1=numbers[:]
        num2=numbers[::-1]
        num1.sort()
        left = 0
        right=len(num1)-1
        while left<right:
            if target-num1[right]>num1[left]:
                left+=1
            elif num1[left]+num1[right]==target:
                a=numbers.index(num1[left])
                b=(len(num2)-1)-num2.index(num1[right])
                return [a,b],num1
            else:
                right-=1
        # print(num1)
if __name__ == '__main__':
    li=Solution()
    print(li.twoSum([-1,-2,-3,-4,-5],-8))
    # li.twoSum([3, 3, 2, 1, 6], 7)