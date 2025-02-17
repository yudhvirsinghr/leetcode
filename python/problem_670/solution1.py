class Solution:
    def maximumSwap(self, num: int) -> int:
        # we need to track what is the highest number
        # from the right of current idx

        # convert the int to str
        str_num = list(str(num))
        n = len(str_num)

        max_right_idx = [0] * n
        # last idx will always be same
        max_right_idx[n - 1] = n - 1

        for i in range(n - 2, -1, -1):
            # if the current number is greater than max of the right
            if str_num[i] > str_num[max_right_idx[i + 1]]:
                max_right_idx[i] = i
            # keep the max from right
            else:
                max_right_idx[i] = max_right_idx[i + 1]

        # now we go from left to right
        for j in range(n):
            if str_num[j] < str_num[max_right_idx[j]]:
                str_num[j], str_num[max_right_idx[j]] = str_num[max_right_idx[j]], str_num[j]
                return int("".join(str_num))

        return num
