class Solution(object):
    def reverseWords(self, s):
        list_s=s.split()
        list_s=list_s[::-1]
        output=" ".join(list_s)
        
        return output
