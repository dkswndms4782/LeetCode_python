class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #  따로 할당하는 것 보다 한번에 할당하는게 더 빠름
        tmp = res = sum(nums[:k])
        for i in range(k, len(nums)):
            # tmp += nums[i] - nums[i-k]로도 할 수 있지만 훨씬 느려짐. 따로 연산하는게 더 빠르다!
            tmp += nums[i] 
            tmp -= nums[i-k]
            res = max(res, tmp)
        return res/k