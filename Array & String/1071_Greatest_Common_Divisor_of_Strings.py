class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = list(map(lambda x: ((x + extraCandies) >= max_candies), candies))
        return result