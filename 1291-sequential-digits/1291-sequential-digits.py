class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = [1,2,3,4,5,6,7,8,9]
        res = []
        i = 0
        while i < len(queue):
            if low <= queue[i] <= high:
                res.append(queue[i])
            x = queue[i] % 10 + 1
            candidate = queue[i] * 10 + x 
            if x < 10 and candidate <= high:
                queue.append(candidate)
            i += 1
        return res

            