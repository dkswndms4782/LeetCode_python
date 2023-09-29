class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for idx, i in enumerate(t):
            if len(s) == 0:
                return True
            if s[0] == i:
                s = s[1:]
            t = t[1:]
        if s == "":
            return True
        else:
            return False