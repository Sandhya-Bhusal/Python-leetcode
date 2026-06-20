class Solution(object):
    def leftRightDifference(self, nums):
        total=sum(nums)
        leftSum=0
        output=[]
        rightSum=0
        for i in range(len(nums)):
            rightSum=total-leftSum-nums[i]
            output.append(abs(leftSum-rightSum))
            leftSum+=nums[i]
        
        return output