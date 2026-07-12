class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
        tmp = sorted(arr)
        rank = {tmp[0] : 0}
        cnt = 1
        for i in range(1,len(tmp)):
            if tmp[i] > tmp[i-1]:
                rank[tmp[i]] = cnt
                cnt += 1  
        for i in range(len(arr)):
            arr[i] = rank[arr[i]] + 1
        return arr

        