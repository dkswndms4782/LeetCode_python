class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in set(arr):
            dic[i] = 0
        for i in arr:
            dic[i] += 1
        if len(dic.values()) == len(set(dic.values())):
            return True
        return False