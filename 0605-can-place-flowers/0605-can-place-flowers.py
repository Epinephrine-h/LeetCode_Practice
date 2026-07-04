class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        ok = True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if ok :
                    if i + 1 == len(flowerbed) or flowerbed[i+1] == 0:
                        n -= 1
                        ok = False
                else:
                    ok = True
            else:
                ok = False
        return n <= 0
        