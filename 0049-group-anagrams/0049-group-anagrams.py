class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            ana = "".join(sorted(word))
            if ana not in res:
                res[ana] = []
            res[ana].append(word)
        return list(res.values())