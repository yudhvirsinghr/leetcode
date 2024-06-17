from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # you make set
        nums = set(nums)

        longest = 0

        for i in nums:
            # check if n - 1 exists
            if i - 1 not in nums:
                temp_longest = 1
                start = i

                # now check if we have items in order in set
                while start + 1 in nums:
                    temp_longest += 1
                    start += 1

                longest = max(longest, temp_longest)
        return longest
