class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        p2 = 0
        p1 = 0
        while p2 < len(arr2):
            for i in range(p1, len(arr1)):
                if arr1[i] == arr2[p2]:
                    arr1[p1], arr1[i] = arr1[i], arr1[p1]
                    p1 += 1
            p2 += 1
        arr1[p1:] = sorted(arr1[p1:])
        return arr1
