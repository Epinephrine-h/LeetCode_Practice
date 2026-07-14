class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = set()
        arr.sort(key=lambda x : abs(x))
        for i in arr:
            if  i % 2 == 0 and i / 2 in hashmap:
                return True
            hashmap.add(i)
        return False