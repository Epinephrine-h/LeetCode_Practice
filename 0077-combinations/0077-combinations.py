class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        tmp = [i for i in range(1, k + 1)]
        res = []
        while True:
            res.append(list(tmp))
            i = k - 1
            while tmp[i] == n - k + i + 1:
                i -= 1
            if i < 0:
                return res
            else:
                tmp[i] += 1
                tmp[i+1:] = [x for x in range(tmp[i] + 1, tmp[i] + k - i)]