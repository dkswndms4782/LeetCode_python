import math
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeros, ones, possible_flowers = 0,0,0
        for idx,i in enumerate(flowerbed):
            if i == 0: zeros += 1
            else: 
                possible_flowers += max(math.ceil((zeros - ones - 1) / 2), 0)
                zeros, ones = 0,1
        return (possible_flowers + max(math.ceil((zeros - ones) / 2), 0)) >= n
