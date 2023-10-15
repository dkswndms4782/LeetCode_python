from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        w1 = Counter(word1);w2 = Counter(word2)
        if sorted(list(w1.values())) == sorted(list(w2.values())) and w1.keys() == w2.keys():
            return True
        return False