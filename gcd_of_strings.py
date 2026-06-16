from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        gcd_len=gcd(len(str1),len(str2))
        str=str1[:gcd_len]

        if str1+str2==str2+str1:
            return str
        return ""