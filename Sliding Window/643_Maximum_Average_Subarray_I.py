class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #  ���� �Ҵ��ϴ� �� ���� �ѹ��� �Ҵ��ϴ°� �� ����
        tmp = res = sum(nums[:k])
        for i in range(k, len(nums)):
            # tmp += nums[i] - nums[i-k]�ε� �� �� ������ �ξ� ������. ���� �����ϴ°� �� ������!
            tmp += nums[i] 
            tmp -= nums[i-k]
            res = max(res, tmp)
        return res/k