class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a, b = sum(aliceSizes), sum(bobSizes)
        equal_total = (a + b) // 2
        for num in aliceSizes:
            x = a - num
            if x < equal_total:
                if equal_total - x in bobSizes:
                    return [num, equal_total - x]
        