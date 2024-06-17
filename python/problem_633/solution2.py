class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt_num = c ** 0.5

        int_num = int(str(sqrt_num).split(".")[0])
        sqr_num = int_num ** 2

        if sqr_num == c:
            return True

        # memoization
        mem = set()

        for i in range(int_num, 0, -1):
            sqr_num = i ** 2
            mem.add(sqr_num)
            if c - sqr_num in mem:
                return True
            
        return False
