class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n, i = len(arr), len(arr) - 1
        while i >= 0:
            if arr[i] == 0:     arr.insert(i + 1, 0)
            i -= 1
        while len(arr) > n:     arr.pop()