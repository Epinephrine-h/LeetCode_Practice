class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        combination = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                combination.append(nums2[j])
                j += 1
            else:
                combination.append(nums1[i])
                i += 1
        if i < m:   combination += nums1[i:]
        if j < n:   combination += nums2[j:]
        mid = (m + n) // 2
        if (m + n) % 2 != 0:    return float(combination[mid])
        return (combination[mid-1] + combination[mid])/2
        