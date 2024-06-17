from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        if len(seats) == 1 or len(students) == 0:
            return 0

        # sort seats
        seats.sort()
        students.sort()

        # now get the diff as number of moves
        num_moves = 0
        for i in range(len(seats)):
            num_moves += abs(seats[i] - students[i])

        return num_moves
