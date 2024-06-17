from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums.sort()

        longest = 1
        
        temp_longest = 1
        prev = nums[0]

        for item in nums[1:]:
            if item == prev + 1:
                temp_longest += 1
            elif item == prev:
                temp_longest += 0
            else:
                temp_longest = 1
            prev = item

            if temp_longest > longest:
                longest = temp_longest

        return longest
