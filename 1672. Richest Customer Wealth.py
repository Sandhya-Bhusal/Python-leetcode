class Solution(object):
    def maximumWealth(self, accounts):
        max=0
        
        for i in accounts:
            result=0
            for j in range(len(i)):
                result+=i[j]
            if result>max:
                max=result
        return max
    