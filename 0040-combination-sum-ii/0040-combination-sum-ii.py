class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def Combination(start, sum, tmp):
            if sum >= target:
                if sum == target:   ans.append(tmp)
                return
            for i in range(start, len(candidates)):
                if sum + candidates[i] > target:    break
                if i > start and candidates[i] == candidates[i-1]:  continue
                Combination(i+1, sum + candidates[i], tmp + [candidates[i]])
        Combination(0,0,[])
        return ans