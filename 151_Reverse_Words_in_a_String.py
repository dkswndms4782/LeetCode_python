class Solution:
    def reverseWords(self, s: str) -> str:
        ## My Solution
        '''
        words = s.split()
        result = ""
        for i in range(len(words)-1, -1, -1):
            result += f"{words[i]} "
        return result.rstrip()
        '''
        # Below code means show the reverse
        # print(s.split()[::-1])
        return " ".join(s.split()[::-1])