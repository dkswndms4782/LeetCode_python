class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums) - nums[0]
        pivot_index = 0
        while left_sum != right_sum:
            if pivot_index == len(nums)-1:
                return -1
            left_sum += nums[pivot_index]
            pivot_index += 1
            right_sum -= nums[pivot_index]
            
        return pivot_index