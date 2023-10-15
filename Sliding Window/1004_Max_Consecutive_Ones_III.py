import numpy as np
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros_idx = np.where(np.array(nums) == 0)[0]
        if len(zeros_idx) < k: return len(nums)
        zeros_idx = np.append(zeros_idx, len(nums))
        zeros_idx = np.insert(zeros_idx,0,-1)
        res = 0
        for i in range(k+1, len(zeros_idx)):
            res = max(res, zeros_idx[i] - zeros_idx[i-k-1]-1)
        return res