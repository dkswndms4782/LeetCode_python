class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        for i in range(k):
            if s[i] in ["a","i","e","o","u"]: 
                res += 1
        tmp = res
        for i in range(k, len(s)):
            if s[i-k] in ["a","i","e","o","u"]:
                tmp -= 1
            if s[i] in ["a","i","e","o","u"]:
                tmp += 1
            res = max(tmp, res)
        return res