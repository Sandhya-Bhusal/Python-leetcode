class Solution(object):
    def runningSum(self, nums):
        output=[]
        result=0
        for i in range(len(nums)):
            result=result+nums[i]
            output.append(result)
        return output