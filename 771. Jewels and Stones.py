class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        allowed=set(jewels)
        for ch in stones:
            if ch in allowed:
                count+=1
        return count