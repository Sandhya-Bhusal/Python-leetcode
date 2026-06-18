class Solution(object):
    def reverseVowels(self, s):
        vowel="AEIOUaeiou"
        s=list(s)

        left=0
        right=len(s)-1
        for i in range(len(s)):
            if left>right:
                break
            if s[left] in vowel:
                if s[right] in vowel:
                    temp=s[left]
                    s[left]=s[right]
                    s[right]=temp
                    left+=1
                    right-=1
                else:
                    right-=1
            else:
                left+=1
        result="".join(s)
        return resultS