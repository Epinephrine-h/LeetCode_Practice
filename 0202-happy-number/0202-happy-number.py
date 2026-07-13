class Solution:
    def isHappy(self, n: int) -> bool:
        #crazyRabbit
        def get_next(number):
            total_sum = 0
            while number:
                digit = number % 10
                total_sum += digit * digit
                number = number // 10
            return total_sum
        turtle = n
        rabbit = get_next(n)
        while rabbit != 1 and rabbit != turtle:
            turtle = get_next(turtle)
            rabbit = get_next(get_next(rabbit))
        return rabbit == 1
