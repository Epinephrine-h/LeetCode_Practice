class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = {}
        consider = sorted(score, reverse = True)
        for s in range(len(consider)):
            if s == 0:
                rank[consider[s]] = "Gold Medal"
            elif s == 1:
                rank[consider[s]] = "Silver Medal"
            elif s == 2:
                rank[consider[s]] = "Bronze Medal"
            else:
                rank[consider[s]] = str(s + 1)
        return [rank[s] for s in score]