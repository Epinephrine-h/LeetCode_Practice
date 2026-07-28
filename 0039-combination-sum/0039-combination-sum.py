class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def Combination(start,sum,tmp):
            if sum == target:
                ans.append(tmp)
                return
            if sum > target:    return
            for i in range(start, len(candidates)):
                Combination(i,sum + candidates[i], tmp + [candidates[i]])
        Combination(0,0,[])
        return ans