class Solution:
    # Using binarySearch
    def increasingTriplet(self, nums: List[int]) -> bool:
        # min value
        memorization = [-2**32]
        for case in nums:
            if memorization[-1] < case:
                memorization.append(case)
            else:
                left = 0
                right = len(memorization)
                while right > left:
                    mid = (left + right) // 2
                    if memorization[mid] < case:
                        left = mid + 1
                    else:
                        right = mid
                memorization[right] = case
            if len(memorization) > 3:
                return True
        return False