class Solution:
    def reverseVowels(self, s: str) -> str:
        idx = [i for i in range(len(s)) if s[i] in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']]
        s = list(s)
        for i in range(len(idx)//2):
            s[idx[i]],s[idx[len(idx)-i -1]] = s[idx[len(idx)-i-1]],s[idx[i]]
        return ''.join(s)