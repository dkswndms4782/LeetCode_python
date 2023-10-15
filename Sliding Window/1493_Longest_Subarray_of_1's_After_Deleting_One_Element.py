import numpy as np
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros_idx = np.where(np.array(nums) == 0)[0]
        if len(zeros_idx) == 0 or len(zeros_idx) == 1:
            return len(nums)-1
        zeros_idx = np.append(zeros_idx, len(nums))
        zeros_idx = np.insert(zeros_idx,0,-1)
        res = 0
        for i in range(2, len(zeros_idx)):
            res = max(res, zeros_idx[i] - zeros_idx[i-2]-2)
        return res