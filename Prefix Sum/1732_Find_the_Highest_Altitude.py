class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        now, res = 0,0
        for i in gain:
            now = i + now
            res = max(now, res)
        return res