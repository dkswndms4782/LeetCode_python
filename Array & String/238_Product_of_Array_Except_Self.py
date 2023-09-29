class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ,,,,,,,,,,,,,,,,,
        pre, suf = [1], [1]
        for i in range(1,len(nums)):
            pre.append(nums[i-1] * pre[i-1])
            suf.append(nums[len(nums) - i] * suf[i-1])
        suf.reverse()
        return [i * j for i,j in zip(pre, suf)]