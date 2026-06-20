class Solution(object):
    def runningSum(self, nums):
        output=[]
        result=0
        for i in range(len(nums)):
            if i==0:
                result=nums[i]
            else:
                result=result+nums[i]
            output.append(result)
        return output