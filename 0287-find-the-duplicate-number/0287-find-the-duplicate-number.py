class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        turtle = rabbit = 0
        while True:
            turtle = nums[turtle]
            rabbit = nums[nums[rabbit]]
            if turtle == rabbit:
                break
        rabbit = 0
        while rabbit != turtle:
            rabbit = nums[rabbit]
            turtle = nums[turtle]
        return rabbit