class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        res = float('-inf')
        for i in range(len(citations)):
            res = max(res, min(i + 1, citations[i]))
        return res
