class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a, b = sum(aliceSizes), sum(bobSizes)
        diff = (b - a) // 2
        bobSet = set(bobSizes)
        for num in aliceSizes:
            if num + diff in bobSet:
                return [num, num+diff]
        