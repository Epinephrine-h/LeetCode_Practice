class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:      return "1"
        res, cnt, tmp = [], 0, None
        previousCompression = self.countAndSay(n-1)
        for c in previousCompression:
            if not tmp:
                tmp = c
            if tmp != c:
                res.append(str(cnt))
                res.append(tmp)
                tmp, cnt = c, 1
            else:
                cnt += 1
        res.append(str(cnt))
        res.append(tmp)
        return "".join(res)