class Solution(object):
    def findMissingElements(self, nums):
        minValue=min(nums)
        maxValue=max(nums)
        num=set(nums)
        ans=[]
        for i in range(minValue,maxValue+1):
            if i not in num:
                ans.append(i)

        return ans    
            
        